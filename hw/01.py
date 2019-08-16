#计算字符串最后一个单词长度
s = input()
print(len(s.split()[-1]))  #split 切分，默认 为 所有的空字符，包括空格、换行(\n)、制表符(\t)等。