import markdown
import re
from markdown.extensions import codehilite, toc
import os
from typing import List, Dict
from openai import OpenAI
import base64
import httpx
import json

# OpenRouter API 클라이언트 설정
def get_openai_client():
    """OpenRouter API 클라이언트 생성"""
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("API_KEY"),
    )

def add_heading_ids(html: str, headings: list) -> str:
    """HTML heading 태그에 id 속성 추가"""
    for h in headings:
        # ex) <h2>제목</h2> → <h2 id="anchor">제목</h2>
        pattern = rf'(<h{h["level"]}[^>]*>)(.*?){re.escape(h["title"])}(.*?</h{h["level"]}>)'
        replacement = rf'<h{h["level"]} id="{h["anchor"]}">\g<2>{h["title"]}\g<3>'
        html = re.sub(pattern, replacement, html, count=1)
    return html

def markdown_to_html(text: str) -> str:
    """마크다운 텍스트를 HTML로 변환 (heading에 id 부여)"""
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
    # heading id 부여
    headings = extract_headings(text)
    html_content = add_heading_ids(html_content, headings)
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

async def summarize_with_openrouter(content: str) -> str:
    """OpenRouter API를 사용하여 콘텐츠 요약"""
    print("=== AI 요약 함수 호출됨 ===")
    try:
        if not os.getenv("API_KEY"):
            print("API_KEY가 설정되지 않음")
            return "AI 요약을 사용하려면 API_KEY를 설정해주세요."
        
        print("API_KEY 확인됨")
        
        # 콘텐츠 길이 제한 (API 토큰 제한 고려)
        safe_content = content[:4000] if len(content) > 4000 else content
        
        print(f"원본 길이: {len(content)}, 처리 길이: {len(safe_content)}")
        
        if not safe_content.strip():
            print("콘텐츠가 없음")
            return "요약할 콘텐츠가 없습니다."
        
        print("API 호출 시작...")
        
        # 한글 프롬프트로 복구
        prompt = f"""다음 개발 블로그 포스트를 한국어로 요약해주세요. 주요 기술적 내용과 핵심 포인트를 포함해주세요.

콘텐츠:
{safe_content}"""
        
        # 사용자 예제 코드 그대로 사용
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("API_KEY"),
        )
        
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Dev Blog",
            },
            extra_body={},
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        print("API 호출 완료")
        
        summary_content = completion.choices[0].message.content
        print("요약 성공")
        return f"📝 AI 요약:\n\n{summary_content}"
        
    except Exception as e:
        print(f"에러 발생: {type(e).__name__}: {str(e)}")
        return f"AI 요약 생성 중 오류가 발생했습니다: {str(e)}"

def generate_reading_time(content: str) -> int:
    """예상 읽기 시간 계산 (분)"""
    words = len(content.split())
    # 평균 읽기 속도: 분당 200단어
    reading_time = max(1, round(words / 200))
    return reading_time 