#输入多行，个数n和一系列整数，输出去重排序数组  测试用例不止一组。
#集合（set）是一个无序的不重复元素序列。利用set去重
#python3里input（）默认接收到的是str类型。需要有 转换的过程
#sorted 可以对所有可迭代的对象进行排序操作。list 的 sort 方法返回的
# 是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list
while True:
    try:
        a,res=int(input()),set()   #a即个数，res是set序列
        for i in range(a):
            res.add(int(input()))  #add,集合添加元素
        for i in sorted(res):print(i)  #reverse = True
    except:
        break