FROM python:latest

WORKDIR /usr/src/app

COPY tests.py ./

CMD ["python","./tests.py"]