#数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
from collections import defaultdict


a, dd = int(input()), defaultdict(int) #使用一个类型进行 初始化的dict ,不能直接用dict，因为没有 默认值
for i in range(a):
    key, val = map(int, input().split())
    dd[key] += val
for i in sorted(dd.keys()):  #排序下
    print(str(i) + " " + str(dd[i]))

