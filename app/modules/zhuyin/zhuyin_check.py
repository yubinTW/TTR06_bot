import json

dic = {}

with open('app/modules/zhuyin/data.json',encoding='utf-8') as FILE:
    dic = json.load(FILE)

# check one word


def check(text):
    return True
    leng = len(text)
    if leng == 2:
        if text[0] in dic:
            if text[1] in dic[text[0]]:
                return True
        return False
    elif leng == 3:
        if text[0] in dic:
            if text[1] in dic[text[0]]:
                if text[2] in dic[text[0]][text[1]]:
                    return True
        return False
    elif leng == 4:
        if text[0] in dic:
            if text[1] in dic[text[0]]:
                if text[2] in dic[text[0]][text[1]]:
                    if text[3] in dic[text[0]][text[1]][text[2]]:
                        return True
        return False
    else:
        print('error: texts not in 2~4 length')
        return False


if __name__ == '__main__':
    text = str(input())
    print(check(text))
