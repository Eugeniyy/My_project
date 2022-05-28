FROM python:3.10.4-slim
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY /mysite/ /usr/src/app/