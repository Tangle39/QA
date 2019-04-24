# 统计日志文件error的数量
with open('/Users/lu/Documents/Code/QA/study/py/3/test.log') as f:
    # 用with语句的好处，就是到达语句末尾时，会自动关闭文件，即便出现异常。
    a = f.read()
    '''
     #read读取整个文件
     readline    　特点：readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存

　　缺点：比readlines慢得多
    readlines   读取整个文件到一个迭代器以供我们遍历（读取到一个list中，以供使用，比较方便
    '''

    s = a.count('error')
    print(s)

with open('/Users/lu/Documents/Code/QA/study/py/3/test.log') as f:
    s = 0
    for line in f.readlines():
        s += line.count('error')
    print(s)
