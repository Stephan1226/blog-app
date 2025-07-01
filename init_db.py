#!/usr/bin/env python3
"""
데이터베이스 초기화 스크립트
개발 블로그 샘플 사용자와 포스트를 생성합니다.
"""

import os
import sys
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Post
from crud import user_crud, post_crud
from schemas import UserCreate, PostCreate

def init_db():
    """데이터베이스 초기화"""
    print("데이터베이스 테이블을 생성합니다...")
    Base.metadata.create_all(bind=engine)
    print("✅ 데이터베이스 테이블 생성 완료")

def create_sample_data():
    """샘플 데이터 생성"""
    db = SessionLocal()
    try:
        # 샘플 사용자 생성
        print("샘플 사용자를 생성합니다...")
        sample_user = UserCreate(
            username="developer",
            email="developer@example.com",
            password="dev123456"
        )
        
        # 기존 사용자 확인
        existing_user = user_crud.get_user_by_email(db, sample_user.email)
        if not existing_user:
            user = user_crud.create_user(db, sample_user)
            print(f"✅ 사용자 생성 완료: {user.username}")
        else:
            user = existing_user
            print(f"✅ 기존 사용자 사용: {user.username}")
        
        # 마크다운 샘플 포스트 생성
        print("개발 블로그 샘플 포스트를 생성합니다...")
        sample_posts = [
            {
                "title": "FastAPI로 현대적인 개발 블로그 구축하기",
                "content": """# FastAPI로 현대적인 개발 블로그 구축하기

안녕하세요! 이번 포스트에서는 **FastAPI**를 사용하여 현대적인 개발 블로그를 구축하는 과정을 공유하겠습니다.

## 🚀 왜 FastAPI인가?

FastAPI는 Python 3.7+을 기반으로 한 현대적이고 빠른 웹 프레임워크입니다. 다음과 같은 장점들이 있습니다:

- **높은 성능**: NodeJS와 Go와 비슷한 수준의 성능
- **빠른 개발**: 직관적인 API 설계로 개발 속도 향상
- **자동 문서화**: OpenAPI와 Swagger UI 자동 생성
- **타입 힌트 지원**: Python 타입 힌트 기반의 검증과 직렬화

## 📋 주요 기능들

이 블로그에서 구현한 주요 기능들은 다음과 같습니다:

### 1. 마크다운 지원
```python
import markdown

def markdown_to_html(text: str) -> str:
    md = markdown.Markdown(
        extensions=['codehilite', 'toc', 'fenced_code', 'tables']
    )
    return md.convert(text)
```

### 2. 다크모드 토글
CSS 변수를 활용한 다크모드 구현:

```css
:root {
    --bg-color: #f8f9fa;
    --text-color: #212529;
}

[data-theme="dark"] {
    --bg-color: #121212;
    --text-color: #e9ecef;
}
```

### 3. AI 요약 기능
OpenRouter API를 활용한 포스트 자동 요약:

```python
from openai import OpenAI

async def summarize_with_openrouter(content: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("API_KEY")
    )
    response = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "개발 블로그"
        },
        model="deepseek/deepseek-r1-0528:free",
        messages=[{"role": "user", "content": f"다음 글을 요약해주세요: {content}"}]
    )
    return response.choices[0].message.content
```

## 🛠️ 기술 스택

| 기술 | 용도 | 버전 |
|------|------|------|
| FastAPI | 백엔드 프레임워크 | 0.104.1 |
| SQLAlchemy | ORM | 2.0.23 |
| MySQL | 데이터베이스 | 8.0 |
| Jinja2 | 템플릿 엔진 | 3.1.2 |
| Docker | 컨테이너화 | Latest |

## 📝 개발 과정에서 배운 점

1. **마크다운 렌더링**: Python-Markdown 라이브러리를 사용해 서버 사이드에서 렌더링
2. **다크모드 구현**: CSS 변수와 JavaScript를 조합한 테마 시스템
3. **AI 통합**: OpenRouter API를 활용한 콘텐츠 요약 기능

## 🔗 유용한 링크

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [SQLAlchemy 문서](https://docs.sqlalchemy.org/)
- [Python-Markdown](https://python-markdown.github.io/)

## 마무리

FastAPI는 정말 강력하고 사용하기 쉬운 프레임워크입니다. 특히 자동 문서화와 타입 힌트 지원이 개발 경험을 크게 향상시켜줍니다.

다음 포스트에서는 Docker를 활용한 배포 과정을 다뤄보겠습니다! 🚀"""
            },
            {
                "title": "Docker로 개발 환경 표준화하기",
                "content": """# Docker로 개발 환경 표준화하기

개발팀의 생산성을 높이는 가장 확실한 방법 중 하나는 **일관된 개발 환경**을 구축하는 것입니다. Docker를 활용하면 이를 쉽게 달성할 수 있습니다.

## 🤔 왜 Docker인가?

### Before Docker 😰
- "내 컴퓨터에서는 잘 되는데요?"
- 복잡한 환경 설정 과정
- OS별 다른 설치 방법
- 라이브러리 버전 충돌

### After Docker 😊
- 모든 환경에서 동일한 실행
- 한 번의 설정으로 모든 곳에서 사용
- 격리된 환경으로 충돌 방지
- 쉬운 배포와 확장

## 📦 프로젝트 Docker 구성

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mysql+pymysql://blog_user:blog_password@db:3306/blog_db
    depends_on:
      - db
    volumes:
      - .:/app
    networks:
      - blog-network

  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: blog_db
      MYSQL_USER: blog_user
      MYSQL_PASSWORD: blog_password
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - blog-network

volumes:
  mysql_data:

networks:
  blog-network:
    driver: bridge
```

## 🚀 실행하기

### 1. 개발 환경 시작
```bash
# 전체 스택 실행
docker-compose up --build

# 백그라운드 실행
docker-compose up -d
```

### 2. 개별 서비스 관리
```bash
# 로그 확인
docker-compose logs -f app

# 컨테이너 상태 확인
docker-compose ps

# 서비스 중지
docker-compose down
```

### 3. 데이터베이스 관리
```bash
# MySQL 컨테이너 접속
docker-compose exec db mysql -u blog_user -p blog_db

# 데이터베이스 백업
docker-compose exec db mysqldump -u root -p blog_db > backup.sql
```

## 💡 Docker 최적화 팁

### 1. 멀티 스테이지 빌드
```dockerfile
# 빌드 스테이지
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 실행 스테이지
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. .dockerignore 활용
```
.git
.gitignore
README.md
Dockerfile
.dockerignore
.pytest_cache
.coverage
.env
```

### 3. 헬스체크 추가
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
  CMD curl -f http://localhost:8000/health || exit 1
```

## 🔧 개발 워크플로우

1. **코드 변경** → 자동 리로드
2. **의존성 추가** → `docker-compose build`
3. **데이터베이스 변경** → `docker-compose down -v && docker-compose up`
4. **프로덕션 배포** → `docker build` → 레지스트리 푸시

## 📊 성과 측정

Docker 도입 후 다음과 같은 개선 효과를 얻었습니다:

- ⚡ 새 개발자 온보딩 시간: **2일 → 30분**
- 🐛 환경 관련 버그: **80% 감소**
- 🚀 배포 시간: **30분 → 5분**
- 📈 개발 팀 만족도: **크게 향상**

## 다음 단계

Docker를 더 효과적으로 활용하기 위한 다음 단계들:

1. **Kubernetes** 클러스터 구성
2. **CI/CD** 파이프라인 통합
3. **모니터링** 시스템 구축
4. **보안** 강화 (이미지 스캔, 시크릿 관리)

Docker는 단순한 컨테이너화 도구를 넘어서 개발 문화를 변화시키는 강력한 도구입니다! 🐳"""
            },
            {
                "title": "SQLAlchemy ORM 완벽 가이드",
                "content": """# SQLAlchemy ORM 완벽 가이드

**SQLAlchemy**는 Python에서 가장 강력하고 유연한 ORM(Object-Relational Mapping) 라이브러리입니다. 이번 포스트에서는 실무에서 활용할 수 있는 SQLAlchemy 패턴들을 소개합니다.

## 🏗️ 모델 설계 패턴

### 1. 기본 모델 구조
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 관계 설정
    posts = relationship("Post", back_populates="author")
```

### 2. 고급 관계 설정
```python
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 다대일 관계
    author = relationship("User", back_populates="posts")
    
    # 다대다 관계 (태그 시스템)
    tags = relationship("Tag", secondary="post_tags", back_populates="posts")
```

## 🔍 효율적인 쿼리 패턴

### 1. N+1 문제 해결
```python
# 잘못된 방법 (N+1 문제 발생)
def get_posts_bad():
    posts = session.query(Post).all()
    for post in posts:
        print(post.author.username)  # 각 포스트마다 추가 쿼리

# 올바른 방법 (즉시 로딩)
def get_posts_good():
    posts = session.query(Post).options(joinedload(Post.author)).all()
    for post in posts:
        print(post.author.username)  # 단일 쿼리로 해결
```

### 2. 동적 필터링
```python
def get_posts_filtered(
    title: str = None,
    author_id: int = None,
    created_after: datetime = None
):
    query = session.query(Post)
    
    if title:
        query = query.filter(Post.title.contains(title))
    if author_id:
        query = query.filter(Post.author_id == author_id)
    if created_after:
        query = query.filter(Post.created_at >= created_after)
    
    return query.all()
```

### 3. 페이지네이션
```python
def get_posts_paginated(page: int = 1, per_page: int = 10):
    return session.query(Post)\\
        .order_by(Post.created_at.desc())\\
        .offset((page - 1) * per_page)\\
        .limit(per_page)\\
        .all()
```

## 🛠️ 실무 패턴들

### 1. Repository 패턴
```python
class PostRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, post_data: dict) -> Post:
        post = Post(**post_data)
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post
    
    def get_by_id(self, post_id: int) -> Optional[Post]:
        return self.session.query(Post).filter(Post.id == post_id).first()
    
    def update(self, post_id: int, update_data: dict) -> Optional[Post]:
        post = self.get_by_id(post_id)
        if post:
            for key, value in update_data.items():
                setattr(post, key, value)
            self.session.commit()
            self.session.refresh(post)
        return post
    
    def delete(self, post_id: int) -> bool:
        post = self.get_by_id(post_id)
        if post:
            self.session.delete(post)
            self.session.commit()
            return True
        return False
```

### 2. 트랜잭션 관리
```python
from contextlib import contextmanager

@contextmanager
def db_transaction(session: Session):
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# 사용 예시
def create_post_with_tags(post_data: dict, tag_names: list):
    with db_transaction(SessionLocal()) as session:
        # 포스트 생성
        post = Post(**post_data)
        session.add(post)
        session.flush()  # ID 생성을 위해 flush
        
        # 태그 생성/연결
        for tag_name in tag_names:
            tag = session.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                session.add(tag)
            post.tags.append(tag)
```

### 3. 복잡한 집계 쿼리
```python
from sqlalchemy import func, text

def get_post_statistics():
    return session.query(
        func.count(Post.id).label('total_posts'),
        func.count(func.distinct(Post.author_id)).label('unique_authors'),
        func.avg(func.length(Post.content)).label('avg_content_length'),
        func.max(Post.created_at).label('latest_post_date')
    ).first()

def get_popular_authors():
    return session.query(
        User.username,
        func.count(Post.id).label('post_count')
    ).join(Post)\\
     .group_by(User.id)\\
     .order_by(text('post_count DESC'))\\
     .limit(10).all()
```

## 📊 성능 최적화

### 1. 인덱스 전략
```python
class Post(Base):
    __tablename__ = "posts"
    
    # 복합 인덱스
    __table_args__ = (
        Index('ix_posts_author_created', 'author_id', 'created_at'),
        Index('ix_posts_title_fulltext', 'title', mysql_prefix='FULLTEXT'),
    )
```

### 2. 쿼리 최적화
```python
# 부분 로딩으로 메모리 절약
def get_post_summaries():
    return session.query(Post.id, Post.title, Post.created_at)\\
        .order_by(Post.created_at.desc()).all()

# 배치 로딩으로 성능 향상
def get_posts_with_authors():
    return session.query(Post)\\
        .options(selectinload(Post.author))\\
        .all()
```

### 3. 연결 풀 설정
```python
from sqlalchemy import create_engine

engine = create_engine(
    DATABASE_URL,
    pool_size=20,          # 기본 연결 수
    max_overflow=30,       # 최대 추가 연결 수
    pool_pre_ping=True,    # 연결 상태 확인
    pool_recycle=3600,     # 연결 재사용 시간(초)
    echo=False             # 프로덕션에서는 False
)
```

## 🚀 마이그레이션 관리

### Alembic 설정
```python
# alembic/env.py
from myapp.models import Base

target_metadata = Base.metadata

def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True
        )
        
        with context.begin_transaction():
            context.run_migrations()
```

### 마이그레이션 명령어
```bash
# 새 마이그레이션 생성
alembic revision --autogenerate -m "Add user table"

# 마이그레이션 적용
alembic upgrade head

# 롤백
alembic downgrade -1
```

## 💡 실무 팁

1. **지연 로딩 vs 즉시 로딩**: 대부분 지연 로딩을 사용하고, 필요할 때만 `joinedload`나 `selectinload` 사용
2. **세션 관리**: 요청당 하나의 세션을 사용하고, 적절히 닫기
3. **N+1 문제**: 항상 주의하고, 쿼리 로그를 확인하여 최적화
4. **인덱스**: 자주 검색하는 컬럼에는 인덱스 추가
5. **트랜잭션**: 논리적 단위로 묶어서 관리

SQLAlchemy는 강력하지만 복잡한 도구입니다. 기본기를 탄탄히 하고 점진적으로 고급 기능을 익혀나가세요! 🎯"""
            }
        ]
        
        for post_data in sample_posts:
            # 기존 포스트 확인
            existing_post = db.query(Post).filter(Post.title == post_data["title"]).first()
            if not existing_post:
                post_create = PostCreate(
                    title=post_data["title"],
                    content=post_data["content"],
                    author_id=user.id
                )
                post = post_crud.create_post(db, post_create)
                print(f"✅ 포스트 생성 완료: {post.title}")
            else:
                print(f"✅ 기존 포스트 사용: {existing_post.title}")
        
        print("\n🎉 개발 블로그 샘플 데이터 생성 완료!")
        print(f"📝 생성된 포스트 수: {len(sample_posts)}")
        print("🚀 마크다운, 다크모드, AI 요약 등 다양한 기능을 체험해보세요!")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """메인 함수"""
    print("🚀 개발 블로그 데이터베이스 초기화를 시작합니다...")
    
    try:
        init_db()
        create_sample_data()
        print("\n✅ 데이터베이스 초기화가 완료되었습니다!")
        print("🌐 http://localhost:8000 에서 개발 블로그를 확인하세요.")
        
    except Exception as e:
        print(f"❌ 초기화 중 오류 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 