from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv

from database import get_db, engine
from models import Base, User
from crud import post_crud, user_crud
from schemas import PostCreate, PostUpdate, UserCreate
from utils import markdown_to_html, extract_headings, summarize_with_openrouter, generate_reading_time
from auth import authenticate_user, require_auth, is_authenticated

# 상수 정의
DEFAULT_SECRET_KEY = "your-secret-key-here"
SESSION_MAX_AGE = 3600  # 1시간
DEFAULT_POST_LIMIT = 10
REDIRECT_STATUS_CODE = 303

# 에러 메시지 상수
ERROR_MESSAGES = {
    "post_not_found": "포스트를 찾을 수 없습니다",
    "no_permission_edit": "이 포스트를 수정할 권한이 없습니다",
    "no_permission_delete": "이 포스트를 삭제할 권한이 없습니다",
    "invalid_credentials": "사용자명 또는 비밀번호가 올바르지 않습니다."
}

# 환경 변수 로드
load_dotenv()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="개발 블로그", description="FastAPI로 만든 개발 블로그")

# 세션 미들웨어 추가
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", DEFAULT_SECRET_KEY),
    max_age=SESSION_MAX_AGE
)

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 공통 함수들
def get_base_template_context(request: Request) -> Dict[str, Any]:
    """기본 템플릿 컨텍스트 반환"""
    return {
        "request": request,
        "is_authenticated": is_authenticated(request)
    }

def get_post_or_404(db: Session, post_id: int):
    """포스트를 가져오거나 404 에러 발생"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=ERROR_MESSAGES["post_not_found"]
        )
    return post

def check_post_ownership(post, current_user: User, action: str = "edit"):
    """포스트 소유권 확인"""
    if post.author_id != current_user.id:
        error_key = f"no_permission_{action}"
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ERROR_MESSAGES.get(error_key, f"이 포스트를 {action}할 권한이 없습니다")
        )

def create_template_response(template_name: str, request: Request, **context):
    """템플릿 응답 생성 헬퍼"""
    template_context = get_base_template_context(request)
    template_context.update(context)
    return templates.TemplateResponse(template_name, template_context)

# 라우트 핸들러들
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    """홈페이지 - 최신 포스트 목록"""
    posts = post_crud.get_posts(db, skip=0, limit=DEFAULT_POST_LIMIT)
    
    # 각 포스트에 읽기 시간 추가
    for post in posts:
        post.reading_time = generate_reading_time(post.content)
    
    return create_template_response("index.html", request, posts=posts)

@app.get("/post/{post_id}", response_class=HTMLResponse)
async def read_post(post_id: int, request: Request, db: Session = Depends(get_db)):
    """개별 포스트 읽기"""
    post = get_post_or_404(db, post_id)
    
    # 마크다운을 HTML로 변환
    html_content, toc_html = markdown_to_html(post.content)
    
    # 챕터 목차 생성
    headings = extract_headings(post.content)
    
    # 읽기 시간 계산
    reading_time = generate_reading_time(post.content)
    
    return create_template_response("post.html", request,
        post=post,
        html_content=html_content,
        headings=headings,
        reading_time=reading_time
    )

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    """로그인 폼"""
    if is_authenticated(request):
        return RedirectResponse(url="/", status_code=REDIRECT_STATUS_CODE)
    return create_template_response("login.html", request)

@app.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    """로그인 처리"""
    form = await request.form()
    username = str(form.get("username", ""))
    password = str(form.get("password", ""))
    
    user = authenticate_user(db, username, password)
    if not user:
        return create_template_response("login.html", request, 
            error=ERROR_MESSAGES["invalid_credentials"]
        )
    
    # 세션에 사용자 정보 저장
    request.session["user_id"] = user.id
    request.session["username"] = user.username
    
    return RedirectResponse(url="/", status_code=REDIRECT_STATUS_CODE)

@app.post("/logout")
async def logout(request: Request):
    """로그아웃"""
    request.session.clear()
    return RedirectResponse(url="/", status_code=REDIRECT_STATUS_CODE)

@app.get("/create", response_class=HTMLResponse)
async def create_post_form(request: Request, current_user: User = Depends(require_auth)):
    """새 포스트 작성 폼 (인증 필요)"""
    return create_template_response("create.html", request, current_user=current_user)

@app.post("/create")
async def create_post(
    request: Request, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_auth)
):
    """새 포스트 생성 (인증 필요)"""
    form = await request.form()
    post_data = PostCreate(
        title=str(form.get("title", "")),
        content=str(form.get("content", "")),
        author_id=current_user.id
    )
    post = post_crud.create_post(db, post=post_data)
    return RedirectResponse(url=f"/post/{post.id}", status_code=REDIRECT_STATUS_CODE)

@app.get("/edit/{post_id}", response_class=HTMLResponse)
async def edit_post_form(
    post_id: int, 
    request: Request, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_auth)
):
    """포스트 수정 폼 (인증 필요)"""
    post = get_post_or_404(db, post_id)
    check_post_ownership(post, current_user, "edit")
    
    return create_template_response("edit.html", request, 
        post=post, 
        current_user=current_user
    )

@app.post("/edit/{post_id}")
async def edit_post(
    post_id: int, 
    request: Request, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_auth)
):
    """포스트 수정 (인증 필요)"""
    post = get_post_or_404(db, post_id)
    check_post_ownership(post, current_user, "edit")
    
    form = await request.form()
    post_data = PostUpdate(
        title=str(form.get("title", "")),
        content=str(form.get("content", ""))
    )
    updated_post = post_crud.update_post(db, post_id=post_id, post=post_data)
    return RedirectResponse(url=f"/post/{updated_post.id}", status_code=REDIRECT_STATUS_CODE)

@app.post("/delete/{post_id}")
async def delete_post(
    post_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_auth)
):
    """포스트 삭제 (인증 필요)"""
    post = get_post_or_404(db, post_id)
    check_post_ownership(post, current_user, "delete")
    
    post_crud.delete_post(db, post_id=post_id)
    return RedirectResponse(url="/", status_code=REDIRECT_STATUS_CODE)

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """소개 페이지"""
    return create_template_response("about.html", request)

@app.post("/api/summarize/{post_id}")
async def summarize_post(post_id: int, db: Session = Depends(get_db)):
    """AI를 사용한 포스트 요약"""
    post = get_post_or_404(db, post_id)
    
    try:
        summary_markdown = await summarize_with_openrouter(post.content)
        summary_html, _ = markdown_to_html(summary_markdown)
        return JSONResponse(content={"summary": summary_html})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="요약 생성 중 오류가 발생했습니다."
        )

@app.get("/api/preview")
async def preview_markdown(request: Request):
    """마크다운 미리보기"""
    form = await request.form()
    content = str(form.get("content", ""))
    
    try:
        html_content, _ = markdown_to_html(content)
        return JSONResponse(content={"html": html_content})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="마크다운 변환 중 오류가 발생했습니다."
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 