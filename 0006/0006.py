# 第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import operator
import os
import sys

def get_key(file,
            ignore=(
            '.', '-', ',', ':', ';', '\n', '?', '!', '"', '”', '“', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'),
            lower=True):
    file_object = open(file, 'r')
    txt = file_object.read()
    for i in ignore:
        txt = txt.replace(i, ' ')
    if lower:
        txt = txt.lower()
    words = txt.split(' ')
    dic = {}
    for word in words:
        if word is '':
            continue
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    sort_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    print("The most word in '%s' is '%s',  it appears %s times" % (file, sort_dic[0][0], sort_dic[0][1]))
    print("The second most word in '%s' is '%s',  it appears %s times" % (file, sort_dic[1][0], sort_dic[1][1]))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter. Try to execute 'python 0006.py $dir_path'")
    else:
        for dir_path in sys.argv[1:]:
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                get_key(file_path)
