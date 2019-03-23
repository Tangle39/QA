# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):

        '''  emmm这个也得有table 不然会报错
        输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        中序遍历：首先遍历左子树，然后访问根结点，最后遍历右子树
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
        '''
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))   #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        index = tin.index(root.val)   #索引位置
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root
    #前序遍历&打印值
    def preTr(self,root):

        if root == None:
            return
        print root.val
        self.preTr(root.left)
        self.preTr(root.right)
    #中序
    def inTr(self,root):
        if root is None:
            return
        self.inTr(root.left)
        print root.val
        self.inTr(root.right)
    #后序
    def postTr(self,root):
        if root is None:
            return
        self.postTr(root.left)
        self.postTr(root.right)
        print root.val

# def preTr(root):
#
#     if root == None:
#         return
#     print root.val
#     preTr(root.left)
#     preTr(root.right)

s = Solution()
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
r = s.reConstructBinaryTree(pre,tin)
print r.left    #内存地址 instance：实例
#s.preTr(r)
# preTr(r)
#s.postTr(r)
s.inTr(r)
