FROM python:latest

RUN mkdir -p /usr/src/app

COPY . /usr/src/app/

WORKDIR /usr/src/app

EXPOSE 6000

RUN pip install -r requirements.txt

CMD ./entrypoint.sh
