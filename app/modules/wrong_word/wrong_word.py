import requests
import random
import json
import string

# writing with ass grammer:
# nn mode and None_nn model
# nn: neural network: pick out more wrong_word,
#   but some times would over pickked
# none_nn: pick out less wrong_word, but would not over pickked

# param: url, const string
url = 'http://ckip.iis.sinica.edu.tw/service/typo/api'

# exec when import the file
punctuation_dict = {}
with open('./modules/wrong_word/punctuation.json', 'r') as json_file:
    punctuation_dict = json.load(json_file)


template_single_list = [
    '$ans啦幹',
    '$ans啦幹啦幹',
    '-->$ans<--??ouo???',
    '$ori->$ans'
]

# {}.format(<whole correct str>)
template_str_list = [
    '$str,歐ㄑㄑㄑㄑㄑㄑㄑ'
]


# return string
def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]


# function: split_pun
# brief: split string with punctuation
# param: input: string
# return: {str_list, punctuation_list}
def split_pun(input):
    str_list = []
    temp_str = ''
    punctuation_list = []
    for char in input:
        if char in punctuation_dict:
            punctuation_list.append(char)
            str_list.append(temp_str)
            temp_str = ''
        else:
            temp_str += char
    # end for
    if temp_str != '':
        str_list.append(temp_str)

    return {'str_list': str_list, 'punctuation_list': punctuation_list}


# function: arrange_str_pun
# brief: arrange the string with punctuation
# param: str_list: type: list[string] :brief: the string to arrange
# param: pun_list: type: list[string] :brief: the pun to arrange
def arrange_str_pun(str_list, pun_list):
    output = ''
    str_list_len = len(str_list)
    pun_list_len = len(pun_list)
    for index in range(0, str_list_len):
        output += str_list[index]
        if index < pun_list_len:
            output += pun_list[index]
    return output


# function: arrange_str_pun
# brief: arrange the string with punctuation
# param: str_list: type: list[{'new_str', 'changed_char_list'}]
# param: pun_list: type: list[string] :brief: the pun to arrange
def arrange_str_pun_dic(dic_list, pun_list):
    output = ''
    str_list_len = len(dic_list)
    pun_list_len = len(pun_list)
    for index in range(0, str_list_len):
        output += dic_list[index]['new_str']
        if index < pun_list_len:
            output += pun_list[index]
    return output


# function: render
# param: changed_char_list[]:
#   {'ori': original, 'ans': correct_ans, 'index': index}
# param: correct_str:
# return: rendered string
def render(changed_char_list, correct_str):
    returns = ''

    if len(changed_char_list) == 1:
        # single
        index = random.randint(0, len(template_single_list) - 1)
        template = string.Template(template_single_list[index])
        returns = template.substitute(changed_char_list[0])

    else:
        # multiple
        index = random.randint(0, len(template_str_list) - 1)
        template = string.Template(template_str_list[index])
        returns = template.substitute({'str': correct_str})
    return returns


# function: get_correct_text
# return reply
def get_correct_text(text):
    data_none_nn = {'text': text, 'model': 1}
    data_nn = {'text': text, 'model': 2}

    # http request
    rnn = requests.post(url, json=data_nn)  # nn
    rn_nn = requests.post(url, json=data_none_nn)  # none nn
    # json like string to json, then get text
    rnn_text = json.loads(rnn.text)['corrected']
    rn_nn_text = json.loads(rn_nn.text)['corrected']

    # test print
    print('nn:'+rnn_text)
    print('none nn:'+rn_nn_text)

    # check every char in string
    new_text = ''
    changed_char_list = []  # (ori, correct, index)
    for index in range(0, len(text)):
        ori = text[index]   # original
        ans = ori
        temp_change_dic = {}
        isDifferent = False
        if ori != rnn_text[index]:
            isDifferent = True
            ans = rnn_text[index]

        elif ori != rn_nn_text[index]:
            isDifferent = True
            ans = rn_nn_text[index]

        else:
            isDifferent = False
        # end if

        if isDifferent:
            temp_change_dic = {
                'ori': ori, 'ans': ans, 'index': index
            }
            changed_char_list.append(temp_change_dic)
            # abaaa -> a'b'aaa
            new_text = new_text + '{' + ans + '}'
        else:
            new_text += ans
    # end for
    print('new_text:' + new_text)  # test print
    print('list:', changed_char_list)

    if len(changed_char_list) == 0:
        return None
    else:
        return {'new_str': new_text, 'changed_char_list': changed_char_list}


# function: wrong_word_checker
# brief: check if there's any wrong_word in message, then return reply
# param: input_str: type: string: brief: input string
def wrong_word_checker(input_str):
    # delete space
    input_str = input_str.replace(' ', '')
    # split string with punctuation
    split_dic = split_pun(input_str)  # {'str_list', 'punctuation_list'}
    new_dic_list = []   # {'new_str', 'canged_char_list'}
    wrong_dic_list = []
    wrong_num = 0

    print('split str:', split_dic)  # test

    # check and get correct
    for str in split_dic['str_list']:
        temp = get_correct_text(str)
        if temp is not None:
            wrong_num += 1
            wrong_dic_list.append(temp)
        new_dic_list.append(temp)

    # render string
    if wrong_num == 0:
        return None
    elif wrong_num == 1:
        dic = wrong_dic_list[0]  # {'new_str', 'changed_char_list'}
        wrong_char_dic = dic['changed_char_list'][0]

        index = random.randint(0, len(template_single_list) - 1)
        template = string.Template(template_single_list[index])
        return template.substitute(wrong_char_dic)
    else:
        correct_str = arrange_str_pun_dic(new_dic_list, split_dic['punctuation_list'])
        index = random.randint(0, len(template_str_list) - 1)
        template = string.Template(template_str_list[index])
        return template.substitute({'str': correct_str})


# if main exec code
if __name__ == '__main__':
    text = '在來一次好嗎, 應該不是這樣'

    reply = wrong_word_checker(text)
    print('message reply:'+reply)
