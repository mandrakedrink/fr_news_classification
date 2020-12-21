FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD . .

EXPOSE 80
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app"]
