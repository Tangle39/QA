# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
#最后一个数要有空格
# 质数输出本身
a, res = int(input()), []
for i in range(2, a // 2 + 1):  # //2+1 减少计算量
    while a % i == 0:
        a = a / i
        res.append(i)
print(" ".join(map(str, res)) + " " if res else str(a) + " ")   #if else的一行写法
#map(function, iterable, ...) 这里使用了map将res的数据变成"字符串" Python 3.x 返回迭代器。 而python 2.x返回列表
#str.join(sequence)
#序列中的元素以指定的字符连接生成一个新的字符串。
#print(*objects, sep=' ', end='\n', file=sys.stdout)

# if res:
#     print(" ".join(map(str, res))+" ")
# else:
#     print(str(a) + " ")
