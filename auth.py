from fastapi import HTTPException, status, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import secrets
from typing import Optional
from database import get_db
from crud import user_crud

# 비밀번호 해싱
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# HTTP Basic 인증
security = HTTPBasic()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """비밀번호 검증"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """비밀번호 해싱"""
    return pwd_context.hash(password)

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
    # 세션에서 사용자 ID 확인
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="로그인이 필요합니다",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자를 찾을 수 없습니다",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return user

def require_auth(request: Request, db: Session = Depends(get_db)):
    """인증이 필요한 엔드포인트용 의존성"""
    return get_current_user(request, db)

def is_authenticated(request: Request) -> bool:
    """로그인 상태 확인"""
    return "user_id" in request.session 