FROM python:3.11-slim-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /code

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY src /code

EXPOSE 8000

CMD ["uvicorn", "server.main:app", "--reload", "--host", "0.0.0.0"]
