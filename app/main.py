from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json

from modules.zhuyin.zhuyin import handle_tg_message as zhuyin_handle

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)

def message_handler(bot, update):
    message = update.message.text
    zhuyin_reply = zhuyin_handle(message, update.message.from_user.id)

    if zhuyin_reply != None:
        update.message.reply_markdown(zhuyin_reply)

    

updater = Updater(config['bot_token'])
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()  
print('bot started')
updater.idle()