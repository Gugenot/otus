FROM python:3.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app/ .

EXPOSE 8000

CMD ["uvicorn","main:app","--host=0.0.0.0","--port=8000"]

# Информация по сборке, запуску контейнера и проверке задания: 
# docker build . -t ping
# docker run -p 8000:8000 ping
# curl -X GET http://127.0.0.1:8000/ping
