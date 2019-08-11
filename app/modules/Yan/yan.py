import json
import random
import time
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
import uuid

with open('app/modules/Yan/yan.json', encoding='utf-8') as FILE:
    Data = json.load(FILE)['list']


tags = ""
yans = []
for item in Data:
    tags = tags+"["+item["tag"]+"]"+'\n'
    yans.append(item['yan'])

def post_yan(bot, update):
    query = update.inline_query.query
    if len(query) == 0:
        return
    results = list()
    for i in Data:
        if query in i['tag']:
            for y in i['yan']:
                results.append(
                    InlineQueryResultArticle(
                        id=str(uuid.uuid4()),
                        title=y,
                        input_message_content=InputTextMessageContent(y)
                    )
                )
    print(len(results))
    if len(results) >  40:
        results = results[:40]
    update.inline_query.answer(results)


def helpping(bot, update):
    reply_message = "傳出顏文字:\n `@TTR06_bot <關鍵字>`\n你可以用的關鍵字有:\n\n{}".format(tags)
    update.message.reply_markdown(reply_message)


def showinfo(bot, update):
    reply_message = '*SITCON Camp 2019*\n*Team #6*\n\nMade by:\n - Kenn\n - Yuga Lin\n - An\n - Borm\n - An Jung\n - TIM\n\n隊輔:\n - 去冰\n - 宙斯'
    update.message.reply_markdown(reply_message)
