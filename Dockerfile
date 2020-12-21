FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD . .

EXPOSE 5000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]
