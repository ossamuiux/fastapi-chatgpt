from fastapi import APIRouter

# router 인스턴스
router = APIRouter()


@router.get("/")
def read_root():
    # 딕셔너리 리턴하면 자동으로 json으로 변환하여 응답
    return {"Hello": "World"}
