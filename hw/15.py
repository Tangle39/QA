#输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
print(bin(int(input()))).count('1')   #type(bin())返回为str