#!/bin/bash

echo "🚀 FastAPI 블로그 로컬 개발 환경 실행"
echo "====================================="

# Python 가상환경 확인
if [ ! -d "venv" ]; then
    echo "📦 Python 가상환경을 생성합니다..."
    python3 -m venv venv
fi

# 가상환경 활성화
echo "🔧 가상환경을 활성화합니다..."
source venv/bin/activate

# 의존성 설치
echo "📚 필요한 패키지를 설치합니다..."
pip install -r requirements.txt

# 환경 변수 설정
export DATABASE_URL="mysql+pymysql://blog_user:blog_password@localhost:3306/blog_db"

echo "✅ 로컬 개발 환경이 준비되었습니다!"
echo ""
echo "📝 다음 중 하나를 선택하세요:"
echo "1. MySQL이 로컬에 설치되어 있다면:"
echo "   - MySQL 서버를 시작하세요"
echo "   - 데이터베이스 'blog_db'를 생성하세요"
echo "   - 사용자 'blog_user'를 생성하세요"
echo "   - python init_db.py를 실행하세요"
echo ""
echo "2. Docker로 MySQL만 실행하려면:"
echo "   docker run --name mysql-blog -e MYSQL_ROOT_PASSWORD=root_password -e MYSQL_DATABASE=blog_db -e MYSQL_USER=blog_user -e MYSQL_PASSWORD=blog_password -p 3306:3306 -d mysql:8.0"
echo ""
echo "3. FastAPI 애플리케이션 실행:"
echo "   uvicorn main:app --reload"
echo ""
echo "🌐 웹사이트: http://localhost:8000"
echo "📚 API 문서: http://localhost:8000/docs" 