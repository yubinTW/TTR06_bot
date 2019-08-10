from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging
import json
from modules.Yan.yan import post_yan, helpping, showinfo
from modules.wrong_word.wrong_word import wrong_word_checker
from modules.zhuyin.zhuyin import handle_tg_message as zhuyin_handle

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)


def message_handler(bot, update):
    message = update.message.text

    if message[0] == '/':
        return

    zhuyin_reply = zhuyin_handle(message, update.message.from_user.id)
    if zhuyin_reply is not None:
        update.message.reply_markdown(zhuyin_reply)

    wrong_word_reply = wrong_word_checker(message)
    if wrong_word_reply is not None:
        update.message.reply_text(wrong_word_reply)


updater = Updater(config['bot_token'])
updater.dispatcher.add_handler(CommandHandler('help', helpping))
updater.dispatcher.add_handler(CommandHandler('info', showinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.dispatcher.add_handler(InlineQueryHandler(post_yan))

updater.start_polling()
print('bot started')
updater.idle()
