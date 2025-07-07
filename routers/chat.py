from fastapi import APIRouter
from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# router 인스턴스
router = APIRouter()
# openai 인스턴스
client = OpenAI(api_key=OPENAI_API_KEY)


# 챗요청에 대한 타입
class ChatRequest(BaseModel):
    message: str


# 새로운 응답 생성이므로 post
@router.post("/chat")
def chat(chat: ChatRequest):
    response = client.responses.create(
        model="gpt-4.1-mini",
        # 답변에 대한 지침
        #         instructions="""명확하고 정중하며 전문적인 답변을 제공하세요.
        # 친절한 어조로 간결하게 답변하세요.
        # 질문이 명확하지 않으면 명확하게 설명해 달라고 요청하세요.
        # 항상 고객 만족과 도움을 최우선으로 생각하세요.""",
        instructions="""친근한 반말로 답변하세요.""",
        # role(역할) - developer: 개발자의 지침, 대화맥락에서 유지
        # user: 사용자
        input=[
            {
                "role": "developer",
                "content": "이전 대화를 기억하고 연속적인 답변을 제공하세요.",
            },
            {"role": "user", "content": chat.message},
        ],
    )
    return {"response": response.output_text}
