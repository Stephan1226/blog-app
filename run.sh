#!/bin/bash

echo "🚀 FastAPI 블로그 프로젝트 실행 스크립트"
echo "=========================================="

# Docker가 실행 중인지 확인
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker가 실행되지 않고 있습니다."
    echo "Docker Desktop을 시작한 후 다시 시도해주세요."
    exit 1
fi

echo "✅ Docker가 실행 중입니다."

# 기존 컨테이너 정리
echo "🧹 기존 컨테이너를 정리합니다..."
docker-compose down

# 컨테이너 빌드 및 실행
echo "🔨 컨테이너를 빌드하고 실행합니다..."
docker-compose up --build -d

echo "⏳ 서비스가 시작되는 동안 잠시 기다려주세요..."
sleep 15

# 서비스 상태 확인
echo "📊 서비스 상태를 확인합니다..."
docker-compose ps

echo ""
echo "🎉 블로그가 성공적으로 시작되었습니다!"
echo "🌐 웹사이트: http://localhost:8000"
echo "📚 API 문서: http://localhost:8000/docs"
echo ""
echo "📝 사용법:"
echo "  - 새 글 작성: http://localhost:8000/create"
echo "  - 소개 페이지: http://localhost:8000/about"
echo ""
echo "🛑 서비스를 중지하려면: docker-compose down"
echo "📋 로그를 확인하려면: docker-compose logs -f" 