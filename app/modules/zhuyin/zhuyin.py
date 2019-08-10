import requests
from .zhuyin_engkey_dict import eng_zhuyin_dict
from .zhuyin_check import check
import random
import re

reply_sentences = [
    "你是想說 **\"{correct}\"** 嗎?",
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
    final = []
    sep = re.split(' |6|3|4', input)
    curr_index = 0
    for item in sep:
        curr_index += len(item)+1
        if curr_index > len(input):
            break
        print(curr_index)
        one_text = item+input[curr_index-1]
        print(one_text)
        if not check(one_text):
            print('fail')
            return False

    return True


def handle_tg_message(message, sender_id):
    if message[-1] not in [' ', '6', '3', '4']:
        print('add space')
        message += ' '

    for c in message:
        ord_num = ord(c)
        if not ((ord_num >= 65 and ord_num <= 90) or (ord_num >= 48 and ord_num <= 57)or(ord_num >= 97 and ord_num <= 122)or chr(ord_num) in [' ', '/', ',', '.', ';', '-']):
            return None

    if checkVaildInput(message):
        correct_sentence = engkey_to_words(message)
        if len(correct_sentence) != 0:

            if sender_id not in wrong_count:
                wrong_count[sender_id] = 0
            wrong_count[sender_id] += 1

            reply = random.choice(reply_sentences).format(
                correct=correct_sentence, count=wrong_count[sender_id])

            return reply


if __name__ == '__main__':
    # run tests
    # print(zhuyin_to_words('ㄨㄛˇㄏㄠˇㄜˋ'))
    # print(engkey_to_words('su3cl3'))
    # handle_tg_message('su3cl3', None)
    checkVaildInput('su3cl3')
