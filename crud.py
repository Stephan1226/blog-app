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

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

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

    def verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

# Post CRUD
class PostCRUD:
    def get_post(self, db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()

    def get_posts(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Post).order_by(desc(Post.created_at)).offset(skip).limit(limit).all()

    def get_posts_by_user(self, db: Session, user_id: int, skip: int = 0, limit: int = 100):
        return db.query(Post).filter(Post.author_id == user_id).order_by(desc(Post.created_at)).offset(skip).limit(limit).all()

    def create_post(self, db: Session, post: PostCreate):
        db_post = Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    def update_post(self, db: Session, post_id: int, post: PostUpdate):
        db_post = db.query(Post).filter(Post.id == post_id).first()
        if db_post:
            for key, value in post.dict(exclude_unset=True).items():
                setattr(db_post, key, value)
            db.commit()
            db.refresh(db_post)
        return db_post

    def delete_post(self, db: Session, post_id: int):
        db_post = db.query(Post).filter(Post.id == post_id).first()
        if db_post:
            db.delete(db_post)
            db.commit()
            return True
        return False

# CRUD 인스턴스 생성
user_crud = UserCRUD()
post_crud = PostCRUD() 