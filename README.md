# 현대적인 개발 블로그 프로젝트

**작품명**: 현대적인 개발 블로그 플랫폼  
**작품 주제**: FastAPI와 현대 웹 기술을 활용한 마크다운 지원 개발 블로그 구축  

## 주제 선정 이유
현대적인 웹 개발 기술을 학습하고 실제 운영 가능한 블로그 플랫폼을 구축하기 위해 선정했습니다. FastAPI의 고성능과 Python의 편의성을 활용하여 마크다운 기반의 개발자 친화적인 블로그를 만들고, AI 기술을 접목한 요약 기능으로 사용자 경험을 향상시키고자 했습니다.

## 작품 링크
- **GitHub 링크**: https://github.com/stephankim/fastapi-blog-project
- **배포 링크**: http://localhost:8000 (로컬 개발 환경)

## 프로젝트 설명

### 개발 기간
2024년 12월 - 현재 (진행 중)

### 팀 구성
- **개인 프로젝트**: 풀스택 개발자 (1인)
- **역할**: 백엔드 개발, 프론트엔드 UI/UX, 데이터베이스 설계, DevOps

### 🛠️ 기술 스택

#### **Backend**
- **FastAPI 0.104.1**: 현대적이고 고성능 Python 웹 프레임워크
- **SQLAlchemy 2.0.23**: Python SQL 도구 키트 및 ORM
- **PyMySQL 1.1.0**: Python MySQL 클라이언트 라이브러리
- **Uvicorn**: ASGI 서버 (개발 및 프로덕션)
- **SQLAdmin 0.16.1**: FastAPI용 관리자 인터페이스

#### **Database**
- **MySQL 8.0**: 관계형 데이터베이스 관리 시스템
- **Alembic 1.12.1**: SQLAlchemy 데이터베이스 마이그레이션 도구

#### **Frontend & Template**
- **Jinja2 3.1.2**: 템플릿 엔진
- **Bootstrap 5.1.3**: CSS 프레임워크
- **Font Awesome 6.0.0**: 아이콘 라이브러리
- **Highlight.js**: 코드 구문 강조

#### **Markdown & Content**
- **Python-Markdown 3.5.1**: 마크다운 처리
- **Pygments 2.17.2**: 구문 강조 라이브러리

#### **AI & Integration**
- **OpenRouter API**: AI 기반 콘텐츠 요약 (DeepSeek Chat V3 모델 사용)
- **OpenAI >=1.50.0**: OpenRouter API 호환 클라이언트

#### **Security & Authentication**
- **Passlib[bcrypt] 1.7.4**: 비밀번호 해싱
- **python-jose[cryptography] 3.3.0**: JWT 토큰 처리
- **cryptography 41.0.7**: 암호화 라이브러리

#### **DevOps & Deployment**
- **Docker**: 컨테이너화
- **Docker Compose**: 멀티 컨테이너 애플리케이션 관리

### 📱 실행 화면

#### **홈페이지**
![홈페이지 스크린샷]
- 최신 개발 포스트 목록 표시
- 읽기 시간 표시 및 기술 스택 정보
- 다크모드/라이트모드 토글
- 반응형 디자인으로 모바일 지원

**주요 기능:**
- 포스트 목록 조회 (최신 10개 포스트)
- 검색 기능 (클라이언트 사이드)
- 소셜 링크 (GitHub, LinkedIn)
- 테마 전환 (다크/라이트 모드)
- 포스트별 읽기 시간 자동 계산 (분당 200단어 기준)

#### **포스트 상세 페이지**
![포스트 상세 페이지 스크린샷]
- 마크다운 렌더링된 콘텐츠
- 코드 구문 강조 및 복사 기능
- 챕터별 네비게이션 사이드바
- AI 기반 요약 기능

**주요 기능:**
- 마크다운 완전 지원 (제목, 코드블록, 표, 링크, 줄바꿈 등)
- 목차 자동 생성 및 스무스 스크롤
- 코드 블록 구문 강조 (Pygments 사용)
- OpenRouter AI 요약 (DeepSeek Chat V3 모델)
- 읽기 진행률 표시
- 헤딩에 앵커 링크 자동 생성

#### **포스트 작성/수정 페이지**
![포스트 작성 페이지 스크린샷]
- 실시간 마크다운 미리보기
- 마크다운 문법 도움말
- 폼 유효성 검사

**주요 기능:**
- 실시간 마크다운 미리보기 API 제공
- 마크다운 문법 가이드
- 클라이언트 사이드 유효성 검사
- 사용자 인증 기반 권한 관리
- 세션 기반 로그인 시스템

#### **관리자 페이지**
![관리자 페이지 스크린샷]
- SQLAdmin을 통한 데이터베이스 관리
- 사용자 및 포스트 CRUD 작업
- 웹 기반 관리 인터페이스

**주요 기능:**
- 사용자 관리 (생성, 수정, 삭제)
- 포스트 관리 (일괄 편집, 삭제)
- 데이터베이스 직접 접근 인터페이스
- 관리자 권한 기반 접근 제어

#### **소개 페이지**
![소개 페이지 스크린샷]
- 기술 스택 정보
- 프로젝트 주요 기능 소개
- 개발자 정보

### 📁 프로젝트 폴더 구조

```
project/
├── 📄 main.py                    # FastAPI 메인 애플리케이션
├── 🗄️ database.py               # 데이터베이스 연결 설정
├── 📊 models.py                 # SQLAlchemy 데이터 모델
├── 📋 schemas.py                # Pydantic 스키마 정의
├── 🔧 crud.py                   # CRUD 작업 클래스
├── 🛠️ utils.py                  # 유틸리티 함수 (마크다운, AI)
├── 🔐 auth.py                   # 인증 및 권한 관리
├── 👑 admin.py                  # SQLAdmin 관리자 설정
├── 🚀 init_db.py                # 데이터베이스 초기화 스크립트
├── 👤 create_admin.py           # 관리자 계정 생성 스크립트
├── 📦 requirements.txt          # Python 의존성
├── 🐳 Dockerfile                # Docker 이미지 설정
├── 🐙 docker-compose.yml        # Docker Compose 설정
├── 🐙 docker-compose.dev.yml    # 개발용 Docker Compose 설정
├── ⚙️ env.example                # 환경 변수 예시
├── 🏃 run.sh                    # Docker 실행 스크립트
├── 💻 run_local.sh              # 로컬 개발 실행 스크립트
├── 📚 README.md                 # 프로젝트 문서
├── 🎨 templates/                # Jinja2 템플릿
│   ├── base.html               # 기본 레이아웃
│   ├── index.html              # 홈페이지
│   ├── post.html               # 포스트 상세
│   ├── create.html             # 포스트 작성
│   ├── edit.html               # 포스트 수정
│   ├── login.html              # 로그인 페이지
│   └── about.html              # 소개 페이지
└── 🎭 static/                   # 정적 파일
    ├── css/
    │   └── style.css           # 커스텀 CSS (다크모드 포함)
    └── js/
        └── script.js           # JavaScript 기능들
```

## 💻 소스 코드

### 전체 코드 구조

#### 1. FastAPI 메인 애플리케이션 (main.py)
```python
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
from sqladmin import Admin
from admin import UserAdmin, PostAdmin

# 상수 정의
DEFAULT_SECRET_KEY = "your-secret-key-here"
SESSION_MAX_AGE = 3600
DEFAULT_POST_LIMIT = 10

# 환경 변수 로드
load_dotenv()

# FastAPI 앱 생성
app = FastAPI(title="개발 블로그", description="FastAPI로 만든 개발 블로그")

# Admin 페이지 설정
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)

# 세션 미들웨어 추가
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", DEFAULT_SECRET_KEY),
    max_age=SESSION_MAX_AGE
)

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    """홈페이지 - 최신 포스트 목록"""
    posts = post_crud.get_posts(db, skip=0, limit=DEFAULT_POST_LIMIT)
    
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
    headings = extract_headings(post.content)
    reading_time = generate_reading_time(post.content)
    
    return templates.TemplateResponse("post.html", {
        "request": request,
        "post": post,
        "html_content": html_content,
        "headings": headings,
        "reading_time": reading_time,
        "is_authenticated": is_authenticated(request)
    })

@app.post("/api/summarize/{post_id}")
async def summarize_post(post_id: int, db: Session = Depends(get_db)):
    """AI 포스트 요약"""
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="포스트를 찾을 수 없습니다")
    
    summary = await summarize_with_openrouter(post.content)
    return JSONResponse(content={"summary": summary})
```

#### 2. 데이터베이스 설정 (database.py)
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 데이터베이스 URL 설정
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://blog_user:blog_password@localhost:3306/blog_db")

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    echo=True,  # SQL 쿼리 로깅 (개발용)
    pool_pre_ping=True,  # 연결 상태 확인
    pool_recycle=300,  # 연결 재사용 시간
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 베이스 클래스 생성
Base = declarative_base()

# 데이터베이스 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### 3. 데이터베이스 모델 (models.py)
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 관계 설정
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 관계 설정
    author = relationship("User", back_populates="posts")
```

#### 4. Pydantic 스키마 (schemas.py)
```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User 스키마
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Post 스키마
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    author_id: int

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    author: Optional[User] = None

    class Config:
        from_attributes = True
```

#### 5. CRUD 작업 (crud.py)
```python
from sqlalchemy.orm import Session
from sqlalchemy import desc
from models import User, Post
from schemas import UserCreate, PostCreate, PostUpdate
from passlib.context import CryptContext

# 비밀번호 해싱을 위한 컨텍스트
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User CRUD
class UserCRUD:
    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def create_user(self, db: Session, user: UserCreate):
        hashed_password = pwd_context.hash(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

# Post CRUD
class PostCRUD:
    def get_post(self, db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()

    def get_posts(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Post).order_by(desc(Post.created_at)).offset(skip).limit(limit).all()

    def create_post(self, db: Session, post: PostCreate):
        db_post = Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

# CRUD 인스턴스 생성
user_crud = UserCRUD()
post_crud = PostCRUD()
```

#### 6. 인증 및 권한 (auth.py)
```python
from fastapi import HTTPException, status, Depends, Request
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import get_db
from crud import user_crud

# 비밀번호 해싱
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """비밀번호 검증"""
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    """사용자 인증"""
    user = user_crud.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user(request: Request, db: Session = Depends(get_db)):
    """현재 로그인한 사용자 가져오기"""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="로그인이 필요합니다"
        )
    
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자를 찾을 수 없습니다"
        )
    return user

def require_auth(request: Request, db: Session = Depends(get_db)):
    """인증이 필요한 엔드포인트용 의존성"""
    return get_current_user(request, db)

def is_authenticated(request: Request) -> bool:
    """로그인 상태 확인"""
    return "user_id" in request.session
```

#### 7. 유틸리티 함수 (utils.py)
```python
import markdown
import re
from markdown.extensions import codehilite, toc
import os
from typing import List, Dict
from openai import OpenAI

def markdown_to_html(text: str) -> str:
    """마크다운 텍스트를 HTML로 변환"""
    md = markdown.Markdown(
        extensions=[
            'codehilite',
            'toc',
            'fenced_code',
            'tables',
            'nl2br'
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': True
            },
            'toc': {
                'anchorlink': True,
                'permalink': True,
                'baselevel': 1
            }
        }
    )
    html_content = md.convert(text)
    toc_html = md.toc
    
    # heading id 부여
    headings = extract_headings(text)
    html_content = add_heading_ids(html_content, headings)
    return html_content, toc_html

def extract_headings(markdown_text: str) -> List[Dict[str, str]]:
    """마크다운에서 헤딩을 추출하여 목차 생성"""
    headings = []
    lines = markdown_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            title = line.lstrip('#').strip()
            if title:
                # 앵커 링크 생성
                anchor = re.sub(r'[^\w\s-]', '', title.lower())
                anchor = re.sub(r'[-\s]+', '-', anchor).strip('-')
                
                headings.append({
                    'level': level,
                    'title': title,
                    'anchor': anchor
                })
    
    return headings

async def summarize_with_openrouter(content: str) -> str:
    """OpenRouter API를 사용하여 콘텐츠 요약"""
    try:
        if not os.getenv("API_KEY"):
            return "AI 요약을 사용하려면 API_KEY를 설정해주세요."
        
        # 콘텐츠 길이 제한 (API 토큰 제한 고려)
        safe_content = content[:4000] if len(content) > 4000 else content
        
        prompt = f"""다음 개발 블로그 포스트를 한국어로 요약해주세요:

{safe_content}"""
        
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("API_KEY"),
        )
        
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        summary_content = completion.choices[0].message.content
        return f"📝 AI 요약:\n\n{summary_content}"
        
    except Exception as e:
        return f"AI 요약 생성 중 오류가 발생했습니다: {str(e)}"

def generate_reading_time(content: str) -> int:
    """예상 읽기 시간 계산 (분)"""
    words = len(content.split())
    # 평균 읽기 속도: 분당 200단어
    reading_time = max(1, round(words / 200))
    return reading_time
```

### 템플릿 파일들

#### 8. 기본 레이아웃 (templates/base.html)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Stephan's Dev{% endblock %}</title>
    
    <!-- Beer CSS (Material Design 3) -->
    <link href="https://cdn.jsdelivr.net/npm/beercss@3.11.29/dist/cdn/beer.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    
    <!-- Highlight.js for code syntax highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github.min.css" rel="stylesheet" id="highlight-light">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github-dark.min.css" rel="stylesheet" id="highlight-dark" disabled>
    
    <!-- Custom styles -->
    <link href="{{ url_for('static', path='/css/style.css') }}" rel="stylesheet">
</head>
<body class="light">
    <!-- 네비게이션 바 -->
    <nav class="top">
        <div class="nav-left">
            <a href="/" style="text-decoration:none;color:inherit;"><h6>Stephan's Dev</h6></a>
            <a href="/">홈</a>
            <a href="/about">소개</a>
        </div>
        <div class="nav-right">
            <button id="theme-toggle">
                <i class="material-icons" id="theme-icon">dark_mode</i>
            </button>
            {% if is_authenticated %}
                <span class="user-info">{{ request.session.username }}</span>
                <form method="POST" action="/logout" style="display: inline;">
                    <button type="submit" class="border">로그아웃</button>
                </form>
            {% else %}
                <a href="/login" class="button-primary">로그인</a>
            {% endif %}
            <a href="/admin" class="button-primary">어드민</a>
        </div>
    </nav>

    <!-- 메인 콘텐츠 -->
    <main class="responsive">
        <div class="container">
            {% block content %}{% endblock %}
        </div>
    </main>

    <!-- Beer CSS JavaScript -->
    <script type="module" src="https://cdn.jsdelivr.net/npm/beercss@3.11.29/dist/cdn/beer.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script src="{{ url_for('static', path='/js/script.js') }}"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

#### 9. 홈페이지 (templates/index.html)
```html
{% extends "base.html" %}

{% block content %}
<div class="responsive main-content">
    <div class="content-area">
        <section class="main-posts">
            <h4><i>home</i>최신 포스트</h4>
            
            {% if posts %}
                {% for post in posts %}
                <article class="card">
                    <h5><a href="/post/{{ post.id }}">{{ post.title }}</a></h5>
                    <div class="meta-info">
                        <small>
                            <i>event</i> {{ post.created_at.strftime('%Y년 %m월 %d일') }}
                            {% if post.author %}
                            <i>person</i> {{ post.author.username }}
                            {% endif %}
                            <i>schedule</i> 약 {{ post.reading_time }}분 읽기
                        </small>
                    </div>
                    <p>{{ post.content[:200] }}{% if post.content|length > 200 %}...{% endif %}</p>
                    <div class="actions">
                        <a href="/post/{{ post.id }}">
                            <button><i>arrow_forward</i>읽어보기</button>
                        </a>
                        {% if is_authenticated and post.author and post.author.username == request.session.username %}
                        <a href="/edit/{{ post.id }}">
                            <button class="border"><i>edit</i></button>
                        </a>
                        {% endif %}
                    </div>
                </article>
                {% endfor %}
            {% else %}
                <div class="center-align large-padding">
                    <h4>아직 개발 포스트가 없습니다</h4>
                    <p>첫 번째 개발 포스트를 작성해보세요!</p>
                    {% if is_authenticated %}
                    <a href="/create"><button class="large">첫 포스트 작성하기</button></a>
                    {% endif %}
                </div>
            {% endif %}
        </section>
        
        <aside class="sidebar">
            <article class="card">
                <h6><i>code</i>개발 블로그 소개</h6>
                <p>FastAPI, SQLAlchemy, Jinja2로 구축된 개발 블로그입니다.</p>
                <a href="/about"><button class="border">더 알아보기</button></a>
            </article>
            
            <article class="card">
                <h6><i>edit</i>새 글 작성</h6>
                {% if is_authenticated %}
                <a href="/create"><button>글쓰기</button></a>
                {% else %}
                <a href="/login"><button class="border">로그인</button></a>
                {% endif %}
            </article>
            
            <article class="card">
                <h6><i>build</i>기술 스택</h6>
                <div class="tech-stack">
                    <span class="chip">FastAPI</span>
                    <span class="chip">MySQL</span>
                    <span class="chip">Docker</span>
                    <span class="chip">SQLAlchemy</span>
                </div>
            </article>
        </aside>
    </div>
</div>
{% endblock %}
```

#### 10. 포스트 상세 페이지 (templates/post.html)
```html
{% extends "base.html" %}

{% block content %}
<div class="responsive main-content">
    <div class="content-area">
        <section class="main-posts">
            <article class="card">
                <h4>{{ post.title }}</h4>
                <div class="meta-info">
                    <small>
                        <i>event</i> {{ post.created_at.strftime('%Y년 %m월 %d일 %H:%M') }}
                        {% if post.author %}
                        <i>person</i> {{ post.author.username }}
                        {% endif %}
                        <i>schedule</i> 약 {{ reading_time }}분 읽기
                    </small>
                </div>
                
                <!-- AI 요약 버튼 -->
                <div class="actions" style="margin-bottom: 1rem;">
                    <button class="button-primary" id="ai-summary-btn">
                        <i>smart_toy</i>AI 요약 보기
                    </button>
                </div>
                
                <!-- AI 요약 영역 -->
                <div id="ai-summary" class="card" style="display: none;">
                    <h6><i>smart_toy</i>AI 요약</h6>
                    <div id="summary-content">요약을 생성 중입니다...</div>
                </div>
                
                <!-- 마크다운 콘텐츠 -->
                <div class="markdown-content">
                    {{ html_content | safe }}
                </div>
                
                <div class="actions">
                    <a href="/"><button class="border">목록으로</button></a>
                    {% if is_authenticated and post.author and post.author.username == request.session.username %}
                    <a href="/edit/{{ post.id }}"><button class="border">수정</button></a>
                    {% endif %}
                </div>
            </article>
        </section>
        
        <!-- 목차 사이드바 -->
        <aside class="sidebar post-sidebar">
            {% if headings %}
            <article class="card toc-card">
                <h6><i>list</i>목차</h6>
                <nav class="toc">
                    {% for heading in headings %}
                    <div class="toc-item level-{{ heading.level }}">
                        <a href="#{{ heading.anchor }}" class="toc-link">{{ heading.title }}</a>
                    </div>
                    {% endfor %}
                </nav>
            </article>
            {% endif %}
        </aside>
    </div>
</div>

<script>
// AI 요약 기능
document.getElementById('ai-summary-btn').addEventListener('click', async function() {
    const summaryDiv = document.getElementById('ai-summary');
    const summaryContent = document.getElementById('summary-content');
    
    summaryDiv.style.display = 'block';
    summaryContent.innerHTML = '요약을 생성 중입니다...';
    
    try {
        const response = await fetch(`/api/summarize/{{ post.id }}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await response.json();
        summaryContent.innerHTML = data.summary;
    } catch (error) {
        summaryContent.innerHTML = '요약 생성 중 오류가 발생했습니다.';
    }
});

// 목차 스무스 스크롤
document.querySelectorAll('.toc-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
</script>
{% endblock %}
```

#### 11. 포스트 작성 페이지 (templates/create.html)
```html
{% extends "base.html" %}

{% block content %}
<div class="responsive main-content">
    <div class="content-area">
        <section class="main-posts">
            <div class="write-header">
                <div class="write-toolbar">
                    <button type="button" id="preview-toggle-btn">미리보기</button>
                    <button type="submit" form="post-form" class="primary">발행</button>
                </div>
            </div>
            
            <div class="write-flex">
                <div class="write-form-area">
                    <form method="POST" action="/create" id="post-form">
                        <div class="field">
                            <input type="text" id="title" name="title" placeholder="제목을 입력하세요" required>
                        </div>
                        
                        <!-- 마크다운 툴바 -->
                        <div class="markdown-toolbar">
                            <button type="button" data-md="bold">B</button>
                            <button type="button" data-md="italic">I</button>
                            <button type="button" data-md="code">{}</button>
                            <button type="button" data-md="link">Link</button>
                            <button type="button" data-md="heading">H</button>
                        </div>
                        
                        <div class="field">
                            <textarea id="content" name="content" required rows="15" 
                                placeholder="당신의 이야기를 적어보세요..."></textarea>
                        </div>
                    </form>
                </div>
                
                <!-- 미리보기 영역 -->
                <div class="write-preview-area" id="write-preview-area">
                    <h6>미리보기</h6>
                    <div id="preview-content">
                        <p>내용을 입력하면 미리보기가 표시됩니다.</p>
                    </div>
                </div>
            </div>
        </section>
    </div>
</div>

<script>
// 마크다운 툴바 기능
document.querySelector('.markdown-toolbar').addEventListener('click', function(e) {
    if(e.target.tagName === 'BUTTON') {
        const textarea = document.getElementById('content');
        const type = e.target.getAttribute('data-md');
        const [start, end] = [textarea.selectionStart, textarea.selectionEnd];
        let insert = '';
        
        switch(type) {
            case 'bold': insert = '**굵게**'; break;
            case 'italic': insert = '*기울임*'; break;
            case 'code': insert = '`코드`'; break;
            case 'link': insert = '[텍스트](url)'; break;
            case 'heading': insert = '# 제목'; break;
        }
        
        if(insert) {
            const value = textarea.value;
            textarea.value = value.slice(0, start) + insert + value.slice(end);
            textarea.focus();
        }
    }
});

// 실시간 마크다운 미리보기 (단순 버전)
document.getElementById('content').addEventListener('input', function() {
    const content = this.value;
    const preview = document.getElementById('preview-content');
    
    let html = content;
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>');
    html = html.replace(/\*(.*)\*/gim, '<em>$1</em>');
    html = html.replace(/`([^`]+)`/gim, '<code>$1</code>');
    html = html.replace(/\n/gim, '<br>');
    
    preview.innerHTML = html || '<p>내용을 입력하면 미리보기가 표시됩니다.</p>';
});
</script>
{% endblock %}