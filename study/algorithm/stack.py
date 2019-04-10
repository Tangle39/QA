# -*- coding:utf-8 -*-
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self, node):
        min = self.min()  # 不能用[-1] 因为一开始是空的，会报错
        if not min or node < min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)

    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]


s = Solution()

s.push(2)
s.push(1)
s.push(3)
s.pop()
s.push(6)

print s.stack
print s.assist
print s.top()
print s.min()
