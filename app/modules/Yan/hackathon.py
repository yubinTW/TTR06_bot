import json
import random, time
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle,InputTextMessageContent
import uuid
YanDataPath='yan.json'
file=open(YanDataPath,encoding='utf-8')
info=file.read()
Data=dict(json.loads(info))['list']
def post_yan(bot, update):
    query = update.inline_query.query
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



 