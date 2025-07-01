// 다크모드 관리
class ThemeManager {
    constructor() {
        this.init();
    }
    
    init() {
        // 저장된 테마 로드 또는 시스템 선호도 확인
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        if (savedTheme) {
            this.setTheme(savedTheme);
        } else if (prefersDark) {
            this.setTheme('dark');
        } else {
            this.setTheme('light');
        }
        
        // 테마 토글 버튼 이벤트 (기존 이벤트 리스너 제거 후 추가)
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            // 기존 이벤트 리스너 제거
            themeToggle.removeEventListener('click', this.toggleTheme.bind(this));
            // 새 이벤트 리스너 추가
            themeToggle.addEventListener('click', () => this.toggleTheme());
        }
        
        // 시스템 테마 변경 감지
        window.matchMedia('(prefers-color-scheme: dark)')
            .addEventListener('change', (e) => {
                if (!localStorage.getItem('theme')) {
                    this.setTheme(e.matches ? 'dark' : 'light');
                }
            });
    }
    
    setTheme(theme) {
        const body = document.body;
        
        if (theme === 'dark') {
            body.classList.remove('light');
            body.classList.add('dark');
        } else {
            body.classList.remove('dark');
            body.classList.add('light');
        }
        
        localStorage.setItem('theme', theme);
        this.updateThemeIcon(theme);
        this.updateCodeHighlighting(theme);
        
        // 콘솔에 테마 변경 로그
        console.log(`🌙 테마가 ${theme}로 변경되었습니다.`);
    }
    
    toggleTheme() {
        const currentTheme = document.body.classList.contains('dark') ? 'dark' : 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        this.setTheme(newTheme);
    }
    
    updateThemeIcon(theme) {
        const themeIcon = document.getElementById('theme-icon');
        if (themeIcon) {
            themeIcon.textContent = theme === 'dark' ? 'light_mode' : 'dark_mode';
        }
    }
    
    updateCodeHighlighting(theme) {
        const lightStyle = document.getElementById('highlight-light');
        const darkStyle = document.getElementById('highlight-dark');
        
        if (lightStyle && darkStyle) {
            if (theme === 'dark') {
                lightStyle.disabled = true;
                darkStyle.disabled = false;
            } else {
                lightStyle.disabled = false;
                darkStyle.disabled = true;
            }
        }
    }
}

// 전역 ThemeManager 인스턴스 생성
let themeManager;

// DOM이 로드된 후 ThemeManager 초기화
document.addEventListener('DOMContentLoaded', function() {
    // ThemeManager를 먼저 초기화
    themeManager = new ThemeManager();
    
    // 기본 기능들
    setupFormValidation();
    setupSmoothScroll();
    setupCardHoverEffects();
    
    // 개발 블로그 특화 기능들
    addCodeCopyButtons();
    createReadingProgress();
    setupSearch();
    
    // 코드 하이라이팅 초기화
    if (typeof hljs !== 'undefined') {
        hljs.highlightAll();
    }
    
    console.log('🚀 개발 블로그가 준비되었습니다!');
});

// 폼 유효성 검사
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                    
                    // 커스텀 에러 메시지
                    if (!field.nextElementSibling?.classList.contains('invalid-feedback')) {
                        const errorDiv = document.createElement('div');
                        errorDiv.className = 'invalid-feedback';
                        errorDiv.textContent = '이 필드는 필수입니다.';
                        field.parentNode.insertBefore(errorDiv, field.nextSibling);
                    }
                } else {
                    field.classList.remove('is-invalid');
                    const errorDiv = field.nextElementSibling;
                    if (errorDiv?.classList.contains('invalid-feedback')) {
                        errorDiv.remove();
                    }
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showToast('모든 필수 필드를 입력해주세요.', 'warning');
            }
        });
    });
    
    // 실시간 유효성 검사
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.hasAttribute('required')) {
                if (this.value.trim()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            }
        });
    });
}

// 부드러운 스크롤
function setupSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// 카드 호버 효과
function setupCardHoverEffects() {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// 포스트 삭제 함수
function deletePost(postId) {
    if (confirm('정말로 이 포스트를 삭제하시겠습니까?')) {
        showLoading('포스트를 삭제하고 있습니다...');
        
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/delete/${postId}`;
        document.body.appendChild(form);
        form.submit();
    }
}

// 로딩 인디케이터
function showLoading(message = '처리 중...') {
    const loadingDiv = document.createElement('div');
    loadingDiv.id = 'loading-indicator';
    loadingDiv.className = 'position-fixed top-50 start-50 translate-middle bg-dark text-white p-3 rounded';
    loadingDiv.style.zIndex = '9999';
    loadingDiv.innerHTML = `
        <div class="d-flex align-items-center">
            <div class="spinner-border spinner-border-sm me-2" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            ${message}
        </div>
    `;
    document.body.appendChild(loadingDiv);
}

function hideLoading() {
    const loadingDiv = document.getElementById('loading-indicator');
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

// 토스트 메시지 함수
function showToast(message, type = 'info') {
    const toastContainer = document.querySelector('.toast-container') || createToastContainer();
    
    const toastHtml = `
        <div class="toast align-items-center text-white bg-${type} border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    `;
    
    toastContainer.insertAdjacentHTML('beforeend', toastHtml);
    
    const toastElement = toastContainer.lastElementChild;
    const toast = new bootstrap.Toast(toastElement, {
        autohide: true,
        delay: 5000
    });
    
    toast.show();
    
    // 토스트가 숨겨진 후 DOM에서 제거
    toastElement.addEventListener('hidden.bs.toast', () => {
        toastElement.remove();
    });
}

function createToastContainer() {
    const container = document.createElement('div');
    container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
    container.style.zIndex = '1050';
    document.body.appendChild(container);
    return container;
}

// 코드 복사 기능
function addCodeCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach((codeBlock, index) => {
        const pre = codeBlock.parentElement;
        
        // 복사 버튼이 이미 있는지 확인
        if (pre.querySelector('.copy-button')) return;
        
        const button = document.createElement('button');
        button.className = 'btn btn-sm btn-outline-secondary copy-button position-absolute top-0 end-0 m-2';
        button.innerHTML = '<i class="fas fa-copy"></i>';
        button.title = '코드 복사';
        
        // pre 요소를 relative로 설정
        pre.style.position = 'relative';
        pre.appendChild(button);
        
        button.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(codeBlock.textContent);
                button.innerHTML = '<i class="fas fa-check"></i>';
                button.classList.remove('btn-outline-secondary');
                button.classList.add('btn-success');
                
                setTimeout(() => {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                    button.classList.remove('btn-success');
                    button.classList.add('btn-outline-secondary');
                }, 2000);
                
                showToast('코드가 클립보드에 복사되었습니다!', 'success');
            } catch (err) {
                showToast('코드 복사에 실패했습니다.', 'danger');
            }
        });
    });
}

// 읽기 진행률 표시
function createReadingProgress() {
    // 기존 프로그레스바가 있다면 제거
    const existingProgress = document.getElementById('reading-progress');
    if (existingProgress) {
        existingProgress.remove();
    }
    
    // 기존 컨테이너도 제거
    const existingContainer = document.getElementById('progress-container');
    if (existingContainer) {
        existingContainer.remove();
    }
    
    // 프로그레스바를 fixed position으로 생성
    const progressBar = document.createElement('div');
    progressBar.id = 'reading-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 64px;
        left: 0;
        width: 0%;
        height: 3px;
        background: linear-gradient(to right, #007bff, #28a745);
        transition: width 0.3s ease;
        pointer-events: none;
        user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        box-sizing: border-box;
        z-index: 99;
    `;
    
    document.body.appendChild(progressBar);
    
    // 스크롤 이벤트 최적화
    let ticking = false;
    
    function updateProgress() {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight - windowHeight;
        const scrollTop = window.pageYOffset;
        
        if (documentHeight > 0) {
            const scrollPercentage = (scrollTop / documentHeight) * 100;
            progressBar.style.width = `${Math.min(scrollPercentage, 100)}%`;
        }
        
        ticking = false;
    }
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateProgress);
            ticking = true;
        }
    });
    
    // 초기 진행률 설정
    updateProgress();
}

// 검색 기능 (간단한 클라이언트 사이드 검색)
function setupSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;
    
    const searchResults = document.getElementById('search-results');
    const posts = document.querySelectorAll('.post-item');
    
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase().trim();
        
        if (query === '') {
            posts.forEach(post => post.style.display = 'block');
            if (searchResults) searchResults.innerHTML = '';
            return;
        }
        
        let visibleCount = 0;
        
        posts.forEach(post => {
            const title = post.querySelector('.card-title')?.textContent.toLowerCase() || '';
            const content = post.querySelector('.card-text')?.textContent.toLowerCase() || '';
            
            if (title.includes(query) || content.includes(query)) {
                post.style.display = 'block';
                visibleCount++;
            } else {
                post.style.display = 'none';
            }
        });
        
        if (searchResults) {
            searchResults.innerHTML = `${visibleCount}개의 검색 결과`;
        }
    });
} 