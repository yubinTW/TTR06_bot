FROM python:3.7

WORKDIR /usr/src/app

RUN pip3 install pipenv

COPY . .

RUN pipenv install

CMD [ "pipenv", "run", "python", "app/main.py" ]