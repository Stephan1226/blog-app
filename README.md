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

# 유틸리티 및 모듈 임포트
from utils import markdown_to_html, extract_headings, summarize_with_openrouter, generate_reading_time
from auth import authenticate_user, require_auth, is_authenticated
from sqladmin import Admin

app = FastAPI(title="개발 블로그", description="FastAPI로 만든 개발 블로그")

# SQLAdmin 관리자 페이지 설정
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)

# 세션 미들웨어 및 자동 관리자 계정 생성
# API 엔드포인트들...
```

#### 2. 데이터베이스 모델 (models.py)
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="posts")
```

#### 3. AI 유틸리티 함수 (utils.py)
```python
async def summarize_with_openrouter(content: str) -> str:
    """OpenRouter API를 사용하여 콘텐츠 요약"""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("API_KEY"),
    )
    
    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[{
            "role": "user",
            "content": f"다음 개발 블로그 포스트를 한국어로 요약해주세요: {content[:4000]}"
        }]
    )
    
    return completion.choices[0].message.content
```

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

EXPOSE 8000

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### requirements.txt
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqladmin==0.16.1
sqlalchemy==2.0.23
pymysql==1.1.0
cryptography==41.0.7
jinja2==3.1.2
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
alembic==1.12.1
markdown==3.5.1
pygments==2.17.2
openai>=1.50.0
requests>=2.31.0
httpx>=0.25.0
itsdangerous==2.1.2
```

## 🚀 실행 방법

### Docker Compose로 실행 (권장)
```bash
# 1. 프로젝트 클론
git clone [repository-url]
cd project

# 2. 환경 변수 설정
cp env.example .env
# .env 파일에서 API_KEY 등 설정

# 3. Docker Compose 실행
chmod +x run.sh
./run.sh
```

### 로컬 개발 환경
```bash
# 1. 로컬 실행 스크립트 사용
chmod +x run_local.sh
./run_local.sh

# 2. 수동 설정
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🔧 주요 기능

### 1. 마크다운 지원
- 완전한 마크다운 문법 지원 (제목, 코드블록, 표, 링크)
- 코드 구문 강조 (Pygments)
- 목차 자동 생성
- 실시간 미리보기 API

### 2. AI 기반 요약
- OpenRouter API를 통한 DeepSeek Chat V3 모델 사용
- 포스트 내용 자동 요약
- 한국어 요약 지원

### 3. 사용자 인증
- 세션 기반 로그인 시스템
- 포스트 작성/수정 권한 관리
- 자동 관리자 계정 생성 (system/1234)

### 4. 관리자 기능
- SQLAdmin을 통한 웹 기반 관리 인터페이스
- 사용자 및 포스트 CRUD 작업
- 데이터베이스 직접 관리

### 5. 현대적인 UI/UX
- Bootstrap 5 기반 반응형 디자인
- 다크모드/라이트모드 지원
- 읽기 시간 자동 계산
- 부드러운 스크롤 및 애니메이션

## 🔐 기본 관리자 계정
- **사용자명**: system
- **비밀번호**: 1234
- **권한**: 모든 포스트 작성/수정/삭제 가능

## 📚 API 엔드포인트

### 주요 라우트
- `GET /`: 홈페이지 (포스트 목록)
- `GET /post/{post_id}`: 포스트 상세 보기
- `GET/POST /login`: 로그인
- `GET/POST /create`: 포스트 작성 (인증 필요)
- `GET/POST /edit/{post_id}`: 포스트 수정 (인증 필요)
- `POST /delete/{post_id}`: 포스트 삭제 (인증 필요)
- `GET /about`: 소개 페이지
- `POST /api/summarize/{post_id}`: AI 요약 API
- `GET /api/preview`: 마크다운 미리보기 API
- `/admin`: SQLAdmin 관리자 페이지 