#输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
res = ''
for i in input()[::-1]:
    if i not in res: res += i
print(int(res))