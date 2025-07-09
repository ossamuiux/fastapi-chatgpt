from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 라우터 파일 전체 가져오기
from routers import items, index, chat


# fastapi 인스턴스 생성
app = FastAPI()

# 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 파일별 라우터 인스턴스 포함시키기
app.include_router(items.router)
app.include_router(index.router)
app.include_router(chat.router)
