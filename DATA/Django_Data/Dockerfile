# 베이스 이미지 설정
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt /app/

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update
RUN apt install ffmpeg -y

# 소스 코드 복사
COPY . /app/

# 컨테이너 실행시 실행할 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
