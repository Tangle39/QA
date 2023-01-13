# 递归

程序调用自身的编程技巧称为递归（ recursion）。

一条经典递归例子

```python
def dlc(s):
    """
    数字字母组合 1代表abc...输出输入字符串的所有组合，len = len1*len2*...lenn
    :param s: string like 123
    :return: string like adg
    """
    if not s:
        return None
    d = {'1': ',.?!', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []

    def dfs(tmp, index):
        if index == len(s):  # 出口
            res.append(tmp)
            return

        letters = d.get(s[index])
        for i in letters:
            dfs(tmp + i, index + 1) # 关键步骤

    dfs('', 0)  # 初始化
    return res
```

# Hash

* 定义：把任意长度的输入（又叫做预映射pre-image）通过散列算法变换成固定长度的输出，该输出就是散列值。这种转换是一种压缩映射，也就是，散列值的空间通常远小于输入的空间，不同的输入可能会散列成相同的输出，所以不可能从散列值来确定唯一的输入值。简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。  
1. 基本概念  
若结构中存在和关键字K相等的记录，则必定在f(K)的存储位置上。由此，不需比较便可直接取得所查记录。称这个对应关系f为散列函数(Hash function)，按这个事先建立的表为散列表。  
* 常用的hash函数  
  直接寻址法、数字分析法、平方取中法...  
* 处理冲突方法  
  开放寻址法、再散列法...  
* 哈希函数  
  几个著名的哈希函数：MD2、MD4以及MD5，利用散列法将数字签名转换成的哈希值称为信息摘要(message-digest)，另外还有安全散列算法(SHA)

# 链表

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

## 快慢指针

定义两根指针，移动的速度一快一慢，以此来制造出自己想要的差值。**这个差值可以找到链表上相应的节点**，如找中间值，判断链表中的环

# 图

python的图可以用字典表示

## 图的遍历

### bfs

bfs总是先访问完同一层的结点，然后才继续访问下一层结点，它最有用的性质是可以遍历一次就生成中心结点到所遍历结点的最短路径.

```python
def bfs(adj: dict, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
```

思路：

1 创建一个队列，遍历的起始点放入队列

2 从队列中取出一个元素，打印它，并将其未访问过的子结点放到队列中

3 重复2，直至队列空

### dfs

Depth First Search.其过程简要来说是对每一个可能的分支路径深入到不能再深入为止，而且每个节点只能访问一次.

```python
def dfs(adj: dict, start):
    visited = set()
    stack = [start]
    while stack:
        u = stack.pop()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                stack.append(v)
                visited.add(v)
```

# 树

**树**是一种[数据结构](https://baike.baidu.com/item/数据结构/1450)，它是由*n(n>=1*)个有限结点组成一个具有层次关系的[集合](https://baike.baidu.com/item/集合/2908117)。把它叫做“树”是因为它看起来像一棵倒挂的树，也就是说它是根朝上，而叶朝下的。它具有以下的特点：

每个结点有零个或多个子结点；没有[父结点](https://baike.baidu.com/item/父结点/9796346)的结点称为[根结点](https://baike.baidu.com/item/根结点/9795570)；每一个非根结点有且只有一个父结点

## 二叉查找树

二叉查找树是一种查找效率非常高的数据结构，它有三个特点。

> （1）每个节点最多只有两个子树。
>
> （2）左子树都为小于父节点的值，右子树都为大于父节点的值。
>
> （3）在n个节点中找到目标值，一般只需要log(n)次比较。

## B树

对二叉查找树的改进。它的设计思想是，将相关数据尽量集中在一起，以便一次读取多个数据，减少硬盘操作次数。![img](https://img2018.cnblogs.com/blog/1286166/201810/1286166-20181002222926668-2104350146.png)

 

B树的特点也有三个。

> （1）一个节点可以容纳多个值。比如上图中，最多的一个节点容纳了4个值。
>
> （2）除非数据已经填满，否则不会增加新的层。也就是说，B树追求"层"越少越好。
>
> （3）子节点中的值，与父节点中的值，有严格的大小对应关系。一般来说，如果父节点有a个值，那么就有a+1个子节点。比如上图中，父节点有两个值（7和16），就对应三个子节点