from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="Portfolio API",
    description="포트폴리오 프로젝트용 FastAPI 애플리케이션",
    version="1.0.0"
)

# 응답 모델 정의
class Message(BaseModel):
    message: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# 루트 엔드포인트
@app.get("/", response_model=Message)
async def read_root():
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

# 서버 실행 (개발용)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
