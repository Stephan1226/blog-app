#!/usr/bin/env python3
"""
관리자 계정 생성 스크립트
"""

import os
import sys
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User
from crud import user_crud
from schemas import UserCreate
from auth import get_password_hash

def create_admin_user():
    """관리자 계정 생성"""
    db = SessionLocal()
    try:
        # 관리자 정보 입력 받기
        print("🔐 관리자 계정을 생성합니다.")
        print("=" * 40)
        
        username = input("사용자명을 입력하세요: ").strip()
        if not username:
            print("❌ 사용자명은 필수입니다.")
            return
        
        email = input("이메일을 입력하세요: ").strip()
        if not email:
            print("❌ 이메일은 필수입니다.")
            return
        
        password = input("비밀번호를 입력하세요: ").strip()
        if not password:
            print("❌ 비밀번호는 필수입니다.")
            return
        
        confirm_password = input("비밀번호를 다시 입력하세요: ").strip()
        if password != confirm_password:
            print("❌ 비밀번호가 일치하지 않습니다.")
            return
        
        # 기존 사용자 확인
        existing_user = user_crud.get_user_by_username(db, username)
        if existing_user:
            print(f"❌ 사용자명 '{username}'이 이미 존재합니다.")
            return
        
        existing_email = user_crud.get_user_by_email(db, email)
        if existing_email:
            print(f"❌ 이메일 '{email}'이 이미 존재합니다.")
            return
        
        # 관리자 계정 생성
        admin_user = UserCreate(
            username=username,
            email=email,
            password=password
        )
        
        user = user_crud.create_user(db, admin_user)
        
        print("\n✅ 관리자 계정이 성공적으로 생성되었습니다!")
        print(f"👤 사용자명: {user.username}")
        print(f"📧 이메일: {user.email}")
        print(f"🆔 사용자 ID: {user.id}")
        print("\n🌐 이제 http://localhost:8000/login 에서 로그인할 수 있습니다.")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """메인 함수"""
    print("🚀 관리자 계정 생성 도구")
    print("=" * 40)
    
    try:
        # 데이터베이스 테이블 생성 확인
        Base.metadata.create_all(bind=engine)
        create_admin_user()
        
    except Exception as e:
        print(f"❌ 초기화 중 오류 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 