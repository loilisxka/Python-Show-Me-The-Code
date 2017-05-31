import operator


def get_count_table(file='input.txt',
                    ignore=('.', ',', ':', '?', '!', '"', '”', '“', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'),
                    lower=True):
    txt = open(file).read()
    for i in ignore:
        txt = txt.replace(i, ' ')
    if lower:
        txt = txt.lower()
    words = txt.split(' ')
    # 统计字母出现的个数
    # words = txt.replace(' ','')
    dic = {}
    for word in words:
        if word is '':
            continue
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


print(get_count_table())

result = sorted(get_count_table().items(), key=operator.itemgetter(1), reverse=True)
for item in result:
    print(item[0], item[1])
