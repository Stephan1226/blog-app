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