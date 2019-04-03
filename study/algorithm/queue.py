# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 栈;栈最大的一个特点就是先进后出(FILO—First-In/Last-Out)
# 队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，
# 和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # pop默认删除最后一个
            return self.stack2.pop()

        return self.stack2.pop()


# a= []
# a.append(2)
#
# a.append(3)
#
# a.pop()
# print a
s = Solution()
s.push(4)
s.push(5)
s.push(6)
print s.push(7)
print s.stack1
print s.stack2
print s.pop()
print s.stack2
print s.pop()
print s.stack2
s.push(10)
print s.stack1
print s.stack2
print s.pop()
print s.stack2
print s.stack1
print s.pop()
print s.stack2
print s.pop()
print s.stack2
