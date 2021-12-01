

# 目录

[TOC]

# 基本数据类型

## 列表

### 列表推导式

**[表达式 for 变量 in 序列或迭代对象 if条件]**

for可以有两个来构成循环,详见[product](#product)

```python
# if no annotation, use python 3
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
def letterCombinations(digits: str) -> list:
    KEY = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    if digits == '':
        return []
    ans = ['']
    for num in digits:
        ans = [pre + suf for pre in ans for suf in KEY[num]]
    return ans
```

## 字典

字典在python中非常常用，可以当作哈希表

创建空字典:

```python
c = dict() # 或者
c1 = {}
```

获取字典的键，值

```python
c.keys()  # 此时的类型为dict_keys，可以用list()等进行转换
c.values()
```



# 内建函数

实用内建函数

## join

连接字符串

一般用来连接可迭代对象的各个元素

```python
list=['1','2','3','4','5']
print(''.join(list)) # 12345
```

## format

```python
print('{:.2%}'.format(0.6667)
```

输出百分比，保留两位小数

‘:’用来指定各种格式

```python
print("------Script: {:<3}.py ------".format('sa'))
# 长度大于等于3，否则以空白补齐
print("{:x}".format(16)) # 16进制
```

## 数字相关

### float

```python
print(float(num))  # 3.6e-3 和'3.6e-3'都可以
```

返回一个**十进制浮点型数值（小数）**。

float()括号内可以是三种类型的数据：
1.二进制、八进制、十进制、十六进制的**整数**。`1,0xff,0b111,0o10`
2.bool（布尔值True和False）。
3.表示**十进制**数字的字符串,范围较大。`'32','4e5','.4'...`

特别的，`'inf'`或者`'Infinity'`表示无穷大

### hex

```python
print(int(num))   # 转成10进制,等同于print(num)
print(hex(num))  # 转成16进制
print(bin(num))  # 转成2进制
# num遵循python数字表示法即可
# int还可以将字符串转换成整型:
int('0xA',0)  # 10
```

## enumerate

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标

```python
for i, ch in enumerate(s):
    # ...
```

## sorted()

```python
q = sorted(l) # 排序，返回新列表
# 对字符串操作时
s = 'dca'
print(''.join(sorted(s)))  # ->acd
```

## sort()

``````python
l.sort() # 对原列表进行操作
``````

## zip

将可迭代的对象作为参数，将对象中对应的元素打包成一个个__元组__，然后返回由这些元组组成的对象.

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同

可以利用zip将矩阵对角线的数字互换:(按列从新排)

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[:] = zip(*matrix)
print(matrix)   # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

## map

```python
map(function, iterable, ...) # function -- 函数 iterable -- 一个或多个序列
```

在上面例子中，matrix中元素成了元祖，可以利用map函数;map返回是迭代器，需要用其他函数转换

```python
matrix[:] = map(list, zip(*matrix))  # [:]有隐形转换
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

## 类相关

### setattr

用于设置属性值，该属性不一定是存在的

### hasattr

用于判断对象是否包含对应的属性，有该属性返回 True，否则返回 False。

由`getattr`和exception实现

```python
class A(object):
    b = 6


def main():
    a = A()
    setattr(a, 'c', 7)
    a.d = 8
    print a.c, a.d  # 7 8
    print hasattr(a, 'd') # True
```

[返回目录](#目录)

# 命名空间

**命名空间是对变量名的分组划分**。

LEGB规定了查找一个名称的顺序为：local-->enclosing function locals-->global-->builtin

通过把一些模块进行加载和重命名(库中的类)操作，可以加快查找速度？

# 常用模块

## os

**os** 模块提供了非常丰富的方法用来处理文件和目录

```python
system(command:str) # 在一个子shell执行command命令
```



## collections

### defaultdict

defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值

```python
dict =defaultdict( factory_function)
```

factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0

### Counter

对可迭代对象的各个元素进行计数，统计

```python
s = 'aabbcc'
C = Counter(s) # 此时类型为Counter类，类似于字典
```



## typing

方法参数的类型检查

## itertools

The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.

### permutations

返回可迭代对象的排列，默认全排列

```python
list(permutations(range(3), 2)) --> [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]
```

### product

用于求多个可迭代对象的笛卡尔积(Cartesian Product)，它跟嵌套的 for 循环等价

内部生成元素为tuple

## functools

### reduce

对参数序列中元素进行累积。

```python
# 计算阶乘
def fab(n: int):
    return reduce(lambda x, y: x * y, range(1, n + 1))
```

### wraps

Python[__装饰器__](#装饰器)（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和[docstring](#DocStrings)。

## threading

线程模块

本模块定义了thread的类

创建线程，即从thread继承:

```python
t = threading.Thread(group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None)
# 一般用到target，即自定义的某个函数；args,函数的入参
```

线程运行：

```python
t.start()
```

# multiprocessing

多进程

```python
import multiprocessing
import os
def saku1():
    print('saku1 is called,pid is {}'.format(os.getpid()))
p2 = multiprocessing.Process(target=saku1)   
p2.start()  # 不能直接用run，是假的多进程，几个函数的pid会相同
```

### daemon

设置线程为守护线程

```python
t.setDaemon(True)  # 设置必须要在start之前
```

主线程为非守护线程(前台线程)，当前台线程结束时，守护线程也会结束

## queue

queue 模块即队列，特别适合处理信息在多个线程间安全交换的多线程程序中

### 1 Queue(maxsize=0)

先进先出(First In First Out: FIFO)队列，最早进入队列的数据拥有出队列的优先权

入参 maxsize 是一个整数，用于设置队列的最大长度。一旦队列达到上限，插入数据将会被阻塞，直到有数据出队列之后才可以继续插入。如果 maxsize 设置为小于或等于零，则队列的长度没有限制。

示例如下：

```python
import queue
q = queue.Queue()  # 创建 Queue 队列
for i in range(3):
    q.put(i)  # 在队列中依次插入0、1、2元素
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为0、1、2
```

### 2 LifoQueue(maxsize=0)

后进先出(Last In First Out: LIFO)队列，最后进入队列的数据拥有出队列的优先权，就像栈一样。

入参 maxsize 与先进先出队列的定义一样。

示例如下：

```python
import queue
q = queue.LifoQueue()  # 创建 LifoQueue 队列
for i in range(3):
    q.put(i)  # 在队列中依次插入0、1、2元素
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为2、1、0
```

### 3 PriorityQueue(maxsize=0)

优先级队列，比较队列中每个数据的大小，__值最小的数据__拥有出队列的优先权。数据一般以元组的形式插入，典型形式为(priority_number, data)。如果队列中的数据没有可比性，那么数据将被包装在一个类中，忽略数据值，仅仅比较优先级数字。

示例如下：

```python
import queue
q = queue.PriorityQueue()  # 创建 PriorityQueue 队列
data1 = (1, 'python')
data2 = (2, '-')
data3 = (3, '100')
style = (data2, data3, data1)
for i in style:
    q.put(i)  # 在队列中依次插入元素 data2、data3、data1
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为 data1、data2、data3
```

获取队列元素个数

`q.qsize()`

判断队列是否为空

`q.empty()`

## configparser

对配置文件(ini，cfg)进行操作的模块

示例:

```python
"""
test.ini
[GLOBAL]
CON_NUM=1

[CON_000]
GAPP_VERSION=3
GAPP_APP_TYPE=2
GAPP_LOCAL_SSTY=90
GAPP_LOCAL_LOGICAL_ID=3
GAPP_LOCAL_SSID=3
GAPP_REMOTE_SSTY=30
"""
class MyParser(configparser.ConfigParser):
    # 重写optionform，防止大小写被改变
    def optionxform(self, optionstr):
        return optionstr


c = MyParser()
path = 'test.ini'
c.read(path)
c.set('CON_000', 'GAPP_VERSION', '5')   # 将此字段改成5
with open(path, 'w+') as f:
    c.write(f, space_around_delimiters=False)  # 改完需要写入，False表示‘=’左右无空格
```

## logging



```python
import logging

logger = logging.getLogger('Test_Device')  # 设置logger名称，没有设置则是root
logger.setLevel(level=logging.INFO)  # 设置默认的日志级别,DEBUG才会全部输出
handler = logging.FileHandler("0827.txt", mode='w')  # 设置文件处理的文件名，默认mode:'a',追加
# 创建日志格式对象
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)  # logger日志对象加载FileHandler对象
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
logger.critical("炸了")
```

## struct

用来在c语言中的结构体与python中的字符串之间进行转换，数据一般来自文件或者网络

```python
import struct

values = (1, b'abc', 2.7)
s = struct.Struct('I3sf')  
'''
I:unsigned int 
s:char[]
f:float
'''
p = s.pack(*values)
u = s.unpack(p)

print(s.size)
print(u)
#12 会有字节对齐
#(1, b'abc', 2.700000047683716)
```

## gc

python里gc.collect()命令可以回收没有被使用的空间，但是这个命令还会返回一个数值，是清除掉的垃圾变量的个数

## random

```python
import random


def main():
    l = [1, 2, 3, 4, 5]
    random.shuffle(l)  # 将l中的元素打乱
    print(l)
```

[↑top](#目录)

# 语法解析

1.  a,b = b,a是怎么实现的

**在python中，会在过程中生成一个元组 c，并且c = (b ,a)，然后进行a = c[0] ， b = c[1] 的操作**

2. a,b=b,a+b

先计算=右边的值

## `*`运算符

将不定数量的参数传递给一个函数

```python
def fun(name, *args):
    # print(f'type:{type(args)}' )
    print(f'你好,{name}')
    for i in args:
        print(f'你的宠物有:{i}')
```

本质是将*后面的可迭代对象解包出来

## **DocStrings**

文档字符串是一个重要工具，用于解释文档程序，帮助你的程序文档更加简单易懂。

``````python
def function():
        ''' say something here！
        '''
        pass
 
print (function.__doc__) # 调用 doc    ->say something here！
``````



# 装饰器

在不改变原有功能代码的基础上,添加额外的功能,如用户验证等。有助于让代码更简短

```python
def timefn(fn):
    """计算性能的修饰器"""

    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1: .5f} s")  # print(f...)为格式化输出用法
        return result

    return measure_time
@timefn
def fun(argc):
    pass
```

# 异常处理

```python
try:
    pass
except:
    pass
finally:
    pass
    # finally中的语句一定会被执行
```

assert:用于判断一个表达式，在表达式条件为 false 的时候触发异常。

例如`assert 0`就会触发异常

# 类

## 继承

```python
import queue


class BaseDevice():  # subclassed by RSSP1_DEV
    __deviceName = None
    __deviceId = None  # cannot visit/inherit
    maxQueueSize = 1024  # inherited by RSSP1_DEV
    TimeScenario = None

    def __init__(self, name, id):  # overridden in RSSP1_DEV
        self.__deviceName = name
        self.__deviceId = id
        self.inQ = queue.Queue(self.maxQueueSize)
        self.TimeScenario = []

    def get_device_id(self):
        print('id is 0x%x' % self.__deviceId)


class RSSP1_DEV(BaseDevice):
    cycleMsgID = 99
    __log = None

    def __init__(self, name, id):
        BaseDevice.__init__(self, name, id)


class RAW_DEV(BaseDevice):
    apptype = 3

    def __init__(self, name, id):
        super().__init__(name, id)  # 在单类继承中,不需要父类的名称来调用父类的函数(super用来调父类)


r = RSSP1_DEV('rssp', 0xA)
r.get_device_id()
print(r.maxQueueSize)
ra = RAW_DEV('raw', 2001)
ra.get_device_id()
```
## property
```python
class BaseDevice():
    _deviceName: str = None  # 保护变量，只能自己或子类使用
    __deviceId = None

    def __init__(self, name, id):
        self._deviceName = name
        self.__deviceId = id

    @property
    def device_name(self):
        return self._deviceName

    @property
    def deviceID(self):
        return self.__deviceId


if __name__ == '__main__':
    b = BaseDevice('raw', 0xaa)
    print(b.device_name)
    print(b.deviceID)
```

property使用场景：1.修饰方法，使方法可以像属性一样访问。调用时不用括号

2.与所定义的属性配合使用，这样可以防止属性被修改

property相当于getter，还可以用setter装饰器，对setter进行设置

```python
# python 2.7
class Geeks(object):
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a
```

## 嵌套类 nested class

嵌套类（也叫内类）是在另一个类中定义的。它并不能提高执行时间，但可以通过将相关的类归为一组来帮助程序的可读性和维护，而且还可以将嵌套类隐藏起来，不让外界看到。

```python
class Dept:
    def __init__(self, dname):
        self.dname = dname

    class Prof:
        def __init__(self, pname):
            self.pname = pname

math = Dept("Mathematics")
mathprof = Dept.Prof("Mark")

print(math.dname)
print(mathprof.pname)
'''
out:
Mathematics
Mark
'''
```

## descriptor

如果一个新式类定义了`__get__`, `__set__`,` __delete__`方法中的一个或者多个，那么称之为descriptor

* Dynamic lookups

```python
# python 2.7
import os


class DirectorySize(object):
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()  # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname  # Regular instance attribute


def main():
    s = Directory('song')
    print s.size
    g = Directory('game')
    print g.size


if __name__ == '__main__':
    main()
#  File count is automatically updated according to folder and file numbers
```

## override

如果需要子类使用某方法必须重新自己实现时，子类override，父类使用exception

```python
# python 2.7


class A(object):
    def test(self):
        """
        Main test method that should be overridden by child classes.
        """
        raise NotImplementedError("Test function needs overridden for each test.")


class B(A):
    def test(self):
        # pass
        print 'yes i have implemented this method'


def main():
    b = B()

    b.test()
# 如果B未实现test，则报错

if __name__ == '__main__':
    main()
```

# 算法

## 递归

### 中序遍历

``````python
class Solution: # 递归通用写法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)
        res = []
        dfs(root)
        return res
``````

### 快排

```python
def qsort(nums: List[int]) -> List[int]:
    if len(nums) <= 1: # 指定结束条件
        return nums
    left = [x for x in nums[1:] if x <= nums[0]]
    right = [x for x in nums[1:] if x > nums[0]]
    return qsort(left) + [nums[0]] + qsort(right)
```
## 回溯

回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。回溯也是用递归实现的
```python
'''

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
来源：力扣（LeetCode） 39
'''
def combinationSum(candidates, target):
    res = []

    def helper(nums, target, res_list):
        if target < 0:
            return
        if target == 0:
            res.append(res_list)
        for i, c in enumerate(nums):
            helper(nums[i:], target - c, res_list + [c]) # 解集不能包含重复的组合

    helper(candidates, target, [])
    return res
```

## 二分查找

```python
# 必须按关键字大小有序排列
def bin_search(nums, val):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## 贪心

贪心算法（又称贪婪算法）是指，在对[问题求解](https://baike.baidu.com/item/问题求解/6693186)时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，[算法](https://baike.baidu.com/item/算法/209025)得到的是在某种意义上的局部最优解

```python
''' 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。
可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。
如果可以一直跳到最后，就成功了。
'''
def canJump(nums: List[int]) -> bool:
    k = 0  # k：维护能跳到的最远距离
    for i, j in enumerate(nums):
        if i > k:
            return False
        k = max(k, i + j)
    return True
```





[↑top](#目录)

