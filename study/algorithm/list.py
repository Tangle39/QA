# -*- coding:utf-8 -*-
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)  # 利用insert(0,val)一直在头部插入
            head = head.next
        return l


print 'ok'
node1 = ListNode(90)
node2 = ListNode(34)
node3 = ListNode(89)
node4 = ListNode(77)
node5 = ListNode(23)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
l = s.printListFromTailToHead(node1)
print l
