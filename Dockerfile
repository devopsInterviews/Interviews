FROM python:latest

WORKDIR /usr/app/src

COPY Python/script.py ./

CMD [ "python", "./test.py"]
