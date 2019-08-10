import json
import random, time
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle,InputTextMessageContent
import logging
import uuid
YanDataPath='app/modules/Yan/yan.json'
f=open(YanDataPath,encoding='utf-8')
info=f.read()
Data=dict(json.loads(info))['list']
tags='['
yans=[]
for item in Data:
    tags=tags+"["+item["tag"]+"]"+'\n'
    yans.append(item['yan'])
def post_yan(bot, update):
    query = update.inline_query.query
    if len(query) == 0:
        return
    results=list()
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
    update.inline_query.answer(results)
def helpping(bot,update):
    reply_message="你可以說的有\n\n{}".format(tags)
    update.message.reply_text(reply_message)
def showinfo(bot,update):
    reply_message='made by:Kenn,Yuga Lin,An,Borm,An Jung\n\n隊輔：去冰,宙斯'
    update.message.reply_text(reply_message)
