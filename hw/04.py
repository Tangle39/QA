#连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
#长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
#print('0'*7) ✔️
def printStr(string):
    if len(string) <=8:
        print(string+'0'*(8-len(string)))
    else:
        while len(string) >8:
            print(string[:8]) #切片，不包活string[8]
            string = string[8:]
        print(string + '0' * (8 - len(string)))
printStr(input())
printStr(input())