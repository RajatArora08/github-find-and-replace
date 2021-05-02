FROM python:3.9-alpine

RUN apk add --no-cache git openssh

WORKDIR /app

COPY requirements.txt .
COPY *.py ./

RUN pip install -r requirements.txt
RUN export GIT_PYTHON_REFRESH=quiet

ENTRYPOINT ["python", "main.py"]
