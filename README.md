# TTR06_bot
Telegram bot made by team #6 of 2019 SITCON Camp

## Before you run this bot

### Setup env

* Install Python 3
* Install `pipenv`
```
$ pip install pipenv
```
* Install deps
```
$ pipenv install
```

### Run the bot

```
$ pipenv run python3 ./app/main.py
```

## feature:
- 文字特效
- 你天殺的忘記切輸入法
  - zhuyin
- 再啦幹
  - wrong_word
- 顏文字

## Run with docker
```
cd TTR06_bot
docker build -t team6-server .
docker run --name team6-server -d team6-server
```