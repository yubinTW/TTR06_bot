import json

dics = []

for i in range(1):
    with open('app/modules/zhuyin/data/{}.json'.format(i+1)) as FILE:
        dic = json.load(FILE)
        dics.append(dic)

# check one word
def check_1(texts):
    print(texts)
    dic = dics[0]
    if texts[0] in dic:
        if texts[1] in dic[texts[0]]:
            return True
    return False

# check one word
def check_2(texts):
    print(texts)
    dic = dics[1]
    if texts[0] in dic:
        if texts[1] in dic[texts[0]]:
            return True
        else:
            return False


# check one word
def check_3(texts):
    print(texts)
    dic = dics[2]
    if texts[0] in dic:
        if texts[1] in dic[texts[0]]:
            return True
        else:
            return False


def check(texts):
    leng = len(texts)
    if leng == 2:
        return check_1(texts)
    elif leng == 3:
        return check_1(texts)
    elif leng == 4:
        return check_1(texts)
    else:
        print('error: texts not in 2~4 length')
        return False

if __name__ == '__main__':
    text = str(input())
    print(check(text))