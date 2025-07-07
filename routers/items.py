from fastapi import APIRouter

# Union 타입 가져오기
from typing import Union

# 데이터 유효성 검증 라이브러리에서 BaseModel 클래스 가져오기
from pydantic import BaseModel

# router 인스턴스
router = APIRouter()


# 들어오는 데이터에 대한 타입을 클래스(모델)로 BaseModel상속하여 생성
# None이 없으면 필수, None이 있으면 옵션
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# 경로, 쿼리 파라미터 받기
@router.get("/items/{item_id}")
# q: Union[str, None] = None
# q: 쿼리 파라메터명
# 쿼리 파라메터는 없을 수 있으므로 Union[str, None] 타입으로 선언
# None이 있으면 옵션
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# update_item함수가 데코레이터 내부로 들어간후
# item_id 정수변환, 요청 본문(body) JSON을 Item 모델로 자동 변환
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
