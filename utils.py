import markdown
import re
from markdown.extensions import codehilite, toc
import google.generativeai as genai
import os
from typing import List, Dict

# Gemini AI 설정
genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))

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
                # 앵커 링크 생성 (공백을 -로 변환, 특수문자 제거)
                anchor = re.sub(r'[^\w\s-]', '', title.lower())
                anchor = re.sub(r'[-\s]+', '-', anchor).strip('-')
                
                headings.append({
                    'level': level,
                    'title': title,
                    'anchor': anchor
                })
    
    return headings

async def summarize_with_gemini(content: str) -> str:
    """Gemini AI를 사용하여 콘텐츠 요약"""
    try:
        if not os.getenv("GEMINI_API_KEY"):
            return "AI 요약을 사용하려면 GEMINI_API_KEY를 설정해주세요."
        
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        다음 개발 블로그 글을 한국어로 간단하고 명확하게 요약해주세요. 
        주요 기술적 내용과 핵심 포인트를 포함해주세요.
        
        글 내용:
        {content[:3000]}  # 토큰 제한을 위해 일부만 전송
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"AI 요약 생성 중 오류가 발생했습니다: {str(e)}"

def generate_reading_time(content: str) -> int:
    """예상 읽기 시간 계산 (분)"""
    words = len(content.split())
    # 평균 읽기 속도: 분당 200단어
    reading_time = max(1, round(words / 200))
    return reading_time 