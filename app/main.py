from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
from modules.Yan import post_yan

from modules.wrong_word.wrong_word import wrong_word_checker
from modules.zhuyin.zhuyin import handle_tg_message as zhuyin_handle

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)


def message_handler(bot, update):
    message = update.message.text
    zhuyin_reply = zhuyin_handle(message, update.message.from_user.id)
    wrong_word_reply = wrong_word_checker(message)

    if zhuyin_reply is not None:
        update.message.reply_markdown(zhuyin_reply)
    elif wrong_word_reply is not None:
        update.message.reply_text(wrong_word_reply)


updater = Updater(config['bot_token'])
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.dispatcher.add_handler(InlineQueryHandler(post_yan))

updater.start_polling()
print('bot started')
updater.idle()
