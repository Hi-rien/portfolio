# Portfolio

FastAPI를 사용한 포트폴리오 웹사이트입니다.

## 🚀 기능

- FastAPI 백엔드 서버
- Jinja2 템플릿 엔진
- 정적 파일 서빙 (CSS, JS)
- RESTful API 엔드포인트
- 반응형 웹 디자인

## 📁 프로젝트 구조

```
portfolio/
├── main.py              # FastAPI 애플리케이션
├── requirements.txt     # Python 의존성
├── templates/
│   └── index.html      # 메인 페이지 템플릿
└── static/
    ├── css/
    │   ├── reset.min.css   # CSS 리셋
    │   └── style.css       # 커스텀 스타일
    └── js/
        ├── jquery.min.js   # jQuery 라이브러리
        └── main.js         # 커스텀 JavaScript
```

## 🛠️ 설치 및 실행

### 1. 가상환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate     # Windows
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 서버 실행
```bash
# 방법 1: uvicorn으로 실행 (권장)
uvicorn main:app --reload

# 방법 2: Python으로 직접 실행
python main.py
```

## 🌐 접속 주소

- **메인 페이지:** http://localhost:8000
- **API 문서 (Swagger):** http://localhost:8000/docs
- **API 문서 (ReDoc):** http://localhost:8000/redoc

## 📡 API 엔드포인트

### 웹 페이지
- `GET /` - 메인 페이지 (HTML)

### API
- `GET /api` - API 루트
- `GET /health` - 서버 상태 확인
- `GET /api/projects` - 프로젝트 목록 조회
- `GET /api/contact` - 연락처 정보 조회
- `GET /items/{item_id}` - 아이템 조회
- `POST /items/` - 아이템 생성

## 🛠️ 기술 스택

- **Backend:** FastAPI, Python 3.9+
- **Template Engine:** Jinja2
- **Frontend:** HTML5, CSS3, JavaScript, jQuery
- **Server:** Uvicorn (ASGI)

## 📝 개발 환경

- Python 3.9+
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Jinja2 3.1.2

## 🚀 배포

이 프로젝트는 다음 플랫폼에 배포할 수 있습니다:
- Heroku
- Vercel
- Railway
- DigitalOcean App Platform
- AWS Elastic Beanstalk

## 📞 연락처

프로젝트에 대한 문의사항이 있으시면 언제든 연락주세요!

---

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요! 