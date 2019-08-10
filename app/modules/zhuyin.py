import requests
from zhuyin_engkey_dict import eng_zhuyin_dict
import random

reply_sentences = [
    "你是想說 **{correct}** 嗎?",
    "忘記切輸入法了啦,幫你翻譯\n**{correct}**",
    "這是你第{count}次忘記切換輸入法了唷~~\n**{correct}**"
]

wrong_count = {}


def zhuyin_to_words(zhuyin):
    r = requests.post('http://zhuyin.yubin.tw', json={'text': zhuyin})
    words = r.json()['text']
    return words


def engkey_to_zhuyin(eng_string):
    zhuyin_string = ''
    for c in eng_string:
        # print('{}: {}'.format(c, eng_zhuyin_dict[c]));
        zhuyin_string += eng_zhuyin_dict[c]
    return zhuyin_string


def engkey_to_words(engkey):
    return zhuyin_to_words(engkey_to_zhuyin(engkey))


def checkVaildInput(input):
    return True
    # TODO: add vaild check


def handle_tg_message(message, update):
    sneder_id = update.message.from_user.id
    # sneder_id = "124"
    if checkVaildInput(message):
        correct_sentence = engkey_to_words(message)
        if len(correct_sentence) != 0:

            if sneder_id not in wrong_count:
                wrong_count[sneder_id] = 0
            wrong_count[sneder_id] += 1
            # print('{}: {}'.format(sneder_id,
            #                       wrong_count[sneder_id]))

            reply = random.choice(reply_sentences).format(
                correct=correct_sentence, count=wrong_count[sneder_id])
            # print(reply)
            update.message.reply_text(reply)


if __name__ == '__main__':
    # run tests
    print(zhuyin_to_words('ㄨㄛˇㄏㄠˇㄜˋ'))
    print(engkey_to_words('su3cl3'))
    handle_tg_message('su3cl3', None)
