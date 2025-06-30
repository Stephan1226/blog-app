from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from database import get_db, engine
from models import Base
from crud import post_crud, user_crud
from schemas import PostCreate, PostUpdate, UserCreate
from utils import markdown_to_html, extract_headings, summarize_with_gemini, generate_reading_time
from auth import authenticate_user, require_auth, is_authenticated

# 환경 변수 로드
load_dotenv()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="개발 블로그", description="FastAPI로 만든 개발 블로그")

# 세션 미들웨어 추가
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", "your-secret-key-here"),
    max_age=3600  # 1시간
)

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    """홈페이지 - 최신 포스트 목록"""
    posts = post_crud.get_posts(db, skip=0, limit=10)
    
    # 각 포스트에 읽기 시간 추가
    for post in posts:
        post.reading_time = generate_reading_time(post.content)
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "posts": posts,
        "is_authenticated": is_authenticated(request)
    })

@app.get("/post/{post_id}", response_class=HTMLResponse)
async def read_post(post_id: int, request: Request, db: Session = Depends(get_db)):
    """개별 포스트 읽기"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="포스트를 찾을 수 없습니다")
    
    # 마크다운을 HTML로 변환
    html_content, toc_html = markdown_to_html(post.content)
    
    # 챕터 목차 생성
    headings = extract_headings(post.content)
    
    # 읽기 시간 계산
    reading_time = generate_reading_time(post.content)
    
    return templates.TemplateResponse("post.html", {
        "request": request, 
        "post": post,
        "html_content": html_content,
        "headings": headings,
        "reading_time": reading_time,
        "is_authenticated": is_authenticated(request)
    })

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    """로그인 폼"""
    if is_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    """로그인 처리"""
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    
    user = authenticate_user(db, username, password)
    if not user:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "사용자명 또는 비밀번호가 올바르지 않습니다."
        })
    
    # 세션에 사용자 ID 저장
    request.session["user_id"] = user.id
    request.session["username"] = user.username
    
    return RedirectResponse(url="/", status_code=303)

@app.post("/logout")
async def logout(request: Request):
    """로그아웃"""
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

@app.get("/create", response_class=HTMLResponse)
async def create_post_form(request: Request, current_user = Depends(require_auth)):
    """새 포스트 작성 폼 (인증 필요)"""
    return templates.TemplateResponse("create.html", {
        "request": request,
        "current_user": current_user
    })

@app.post("/create")
async def create_post(request: Request, db: Session = Depends(get_db), current_user = Depends(require_auth)):
    """새 포스트 생성 (인증 필요)"""
    form = await request.form()
    post_data = PostCreate(
        title=form.get("title"),
        content=form.get("content"),
        author_id=current_user.id
    )
    post = post_crud.create_post(db, post=post_data)
    return RedirectResponse(url=f"/post/{post.id}", status_code=303)

@app.get("/edit/{post_id}", response_class=HTMLResponse)
async def edit_post_form(post_id: int, request: Request, db: Session = Depends(get_db), current_user = Depends(require_auth)):
    """포스트 수정 폼 (인증 필요)"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="포스트를 찾을 수 없습니다")
    
    # 본인이 작성한 포스트만 수정 가능
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="이 포스트를 수정할 권한이 없습니다")
    
    return templates.TemplateResponse("edit.html", {
        "request": request, 
        "post": post,
        "current_user": current_user
    })

@app.post("/edit/{post_id}")
async def edit_post(post_id: int, request: Request, db: Session = Depends(get_db), current_user = Depends(require_auth)):
    """포스트 수정 (인증 필요)"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="포스트를 찾을 수 없습니다")
    
    # 본인이 작성한 포스트만 수정 가능
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="이 포스트를 수정할 권한이 없습니다")
    
    form = await request.form()
    post_data = PostUpdate(
        title=form.get("title"),
        content=form.get("content")
    )
    updated_post = post_crud.update_post(db, post_id=post_id, post=post_data)
    return RedirectResponse(url=f"/post/{updated_post.id}", status_code=303)

@app.post("/delete/{post_id}")
async def delete_post(post_id: int, db: Session = Depends(get_db), current_user = Depends(require_auth)):
    """포스트 삭제 (인증 필요)"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="포스트를 찾을 수 없습니다")
    
    # 본인이 작성한 포스트만 삭제 가능
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="이 포스트를 삭제할 권한이 없습니다")
    
    success = post_crud.delete_post(db, post_id=post_id)
    return RedirectResponse(url="/", status_code=303)

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """소개 페이지"""
    return templates.TemplateResponse("about.html", {
        "request": request,
        "is_authenticated": is_authenticated(request)
    })

@app.post("/api/summarize/{post_id}")
async def summarize_post(post_id: int, db: Session = Depends(get_db)):
    """AI를 사용한 포스트 요약"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="포스트를 찾을 수 없습니다")
    
    summary = await summarize_with_gemini(post.content)
    return JSONResponse(content={"summary": summary})

@app.get("/api/preview", response_class=JSONResponse)
async def preview_markdown(request: Request):
    """마크다운 미리보기"""
    form = await request.form()
    content = form.get("content", "")
    
    html_content, _ = markdown_to_html(content)
    return JSONResponse(content={"html": html_content})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 