# 파이썬 공식 이미지 사용
FROM python:3.13-slim

# 작업 디렉토리 설정
WORKDIR /app

# 도커컨테이너가 격리환경이므로 가상환경구성은 필요없음
# 의존성 복사
COPY requirements.txt .

# pip 업그레이드, 의존성 설치
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 현재 폴더의 모든 파일, 폴더를 /app으로 복사
COPY . .

# 실행 명령 (uvicorn으로 FastAPI 앱 구동)
# "--host", "0.0.0.0" - 모든 주소에서 접근가능
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# 포트 오픈 (FastAPI 기본 포트)
EXPOSE 8000