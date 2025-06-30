# 현대적인 개발 블로그 프로젝트

**작품명**: 현대적인 개발 블로그 플랫폼  
**작품 주제**: FastAPI와 현대 웹 기술을 활용한 마크다운 지원 개발 블로그 구축  

## 주제 선정 이유
[여기에 주제 선정 이유를 작성해주세요]

## 작품 링크
- **GitHub 링크**: [여기에 GitHub 링크를 입력해주세요]
- **배포 링크**: [여기에 배포 링크를 입력해주세요 (선택)]

## 프로젝트 설명

### 개발 기간
[개발 기간을 입력해주세요]

### 팀 구성
[팀 구성 및 역할을 입력해주세요]

### 🛠️ 기술 스택

#### **Backend**
- **FastAPI 0.104.1**: 현대적이고 고성능 Python 웹 프레임워크
- **SQLAlchemy 2.0.23**: Python SQL 도구 키트 및 ORM
- **PyMySQL 1.1.0**: Python MySQL 클라이언트 라이브러리
- **Uvicorn**: ASGI 서버 (개발 및 프로덕션)

#### **Database**
- **MySQL 8.0**: 관계형 데이터베이스 관리 시스템
- **Alembic**: SQLAlchemy 데이터베이스 마이그레이션 도구

#### **Frontend & Template**
- **Jinja2 3.1.2**: 템플릿 엔진
- **Bootstrap 5.1.3**: CSS 프레임워크
- **Font Awesome 6.0.0**: 아이콘 라이브러리
- **Highlight.js**: 코드 구문 강조

#### **Markdown & Content**
- **Python-Markdown 3.5.1**: 마크다운 처리
- **Pygments 2.17.2**: 구문 강조 라이브러리

#### **AI & Integration**
- **Google Gemini API**: AI 기반 콘텐츠 요약
- **google-generativeai 0.3.2**: Gemini API Python 클라이언트

#### **Security & Authentication**
- **Passlib**: 비밀번호 해싱
- **python-jose**: JWT 토큰 처리
- **cryptography**: 암호화 라이브러리

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
- 포스트 목록 조회
- 검색 기능 (클라이언트 사이드)
- 소셜 링크 (GitHub, LinkedIn)
- 테마 전환 (다크/라이트 모드)

#### **포스트 상세 페이지**
![포스트 상세 페이지 스크린샷]
- 마크다운 렌더링된 콘텐츠
- 코드 구문 강조 및 복사 기능
- 챕터별 네비게이션 사이드바
- AI 기반 요약 기능

**주요 기능:**
- 마크다운 완전 지원 (제목, 코드블록, 표, 링크 등)
- 목차 자동 생성 및 스무스 스크롤
- 코드 블록 복사 버튼
- Gemini AI 요약
- 읽기 진행률 표시

#### **포스트 작성/수정 페이지**
![포스트 작성 페이지 스크린샷]
- 실시간 마크다운 미리보기
- 마크다운 문법 도움말
- 폼 유효성 검사

**주요 기능:**
- 실시간 마크다운 미리보기
- 마크다운 문법 가이드
- 클라이언트 사이드 유효성 검사
- 자동 저장 (구현 예정)

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
├── 🚀 init_db.py                # 데이터베이스 초기화 스크립트
├── 📦 requirements.txt          # Python 의존성
├── 🐳 Dockerfile                # Docker 이미지 설정
├── 🐙 docker-compose.yml        # Docker Compose 설정
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
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlalchemy.orm import Session

# 마크다운 및 AI 유틸리티 임포트
from utils import markdown_to_html, extract_headings, summarize_with_gemini

app = FastAPI(title="개발 블로그", description="FastAPI로 만든 개발 블로그")

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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
markdown-extensions==0.1.3
google-generativeai==0.3.2
```

## 🚀 실행 방법

### Docker Compose로 실행 (권장)
```bash
# 1. 프로젝트 클론
git clone [repository-url]
cd project

# 2. 환경 변수 설정
cp env.example .env
# .env 파일에서 GEMINI_API_KEY 등 설정

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

## 🌐 접속 정보
- **웹 애플리케이션**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs
- **ReDoc 문서**: http://localhost:8000/redoc

## 개발하면서 느낀점
[개발 과정에서의 경험, 어려웠던 점, 해결 방법, 학습 내용 등을 작성해주세요]

## 향후 계획
[프로젝트 개선 방향, 추가하고 싶은 기능, 학습 계획 등을 작성해주세요] 