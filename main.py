from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import os

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="Portfolio API",
    description="포트폴리오 프로젝트용 FastAPI 애플리케이션",
    version="1.0.0"
)

# 정적 파일 마운트 (CSS, JS, 이미지 등)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 설정
templates = Jinja2Templates(directory="templates")

# 응답 모델 정의
class Message(BaseModel):
    message: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# 메인 페이지 (HTML 템플릿)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API 엔드포인트들
@app.get("/api", response_model=Message)
async def api_root():
    return {"message": "안녕하세요! Portfolio FastAPI 서버입니다."}

# 헬스체크 엔드포인트
@app.get("/health", response_model=Message)
async def health_check():
    return {"message": "서버가 정상적으로 동작중입니다."}

# 아이템 조회 엔드포인트
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# 아이템 생성 엔드포인트
@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# 프로젝트 목록 API (프론트엔드에서 사용)
@app.get("/api/projects")
async def get_projects():
    # 실제로는 데이터베이스에서 가져올 수 있습니다
    projects = [
        {
            "id": 1,
            "name": "FastAPI Portfolio",
            "description": "Python FastAPI로 구축된 포트폴리오 사이트",
            "tech": ["Python", "FastAPI", "HTML/CSS", "JavaScript"],
            "status": "completed"
        },
        {
            "id": 2,
            "name": "React Dashboard",
            "description": "React로 구축된 관리자 대시보드",
            "tech": ["React", "Node.js", "MongoDB"],
            "status": "in_progress"
        },
        {
            "id": 3,
            "name": "Vue.js E-commerce",
            "description": "Vue.js로 구축된 온라인 쇼핑몰",
            "tech": ["Vue.js", "Express", "PostgreSQL"],
            "status": "planning"
        }
    ]
    return {"projects": projects}

# 연락처 정보 API
@app.get("/api/contact")
async def get_contact():
    return {
        "email": "your-email@example.com",
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/yourusername",
        "phone": "+82-10-0000-0000"
    }

# 서버 실행 (개발용)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
