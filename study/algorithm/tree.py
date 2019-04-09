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
        root = TreeNode(pre.pop(0))  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        index = tin.index(root.val)  # 索引位置
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root

    # 前序遍历&打印值
    def preTr(self, root):

        if root == None:
            return
        print root.val
        self.preTr(root.left)
        self.preTr(root.right)

    # 中序
    def inTr(self, root):
        if root is None:
            return
        self.inTr(root.left)
        print root.val
        self.inTr(root.right)

    # 后序
    def postTr(self, root):
        if root is None:
            return
        self.postTr(root.left)
        self.postTr(root.right)
        print root.val

    # 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, A, B):
        if not B:  # B为None时 为True
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)

    # 层序遍历
    '''
    要用队列来实现。
    1. 把根节点入队列
    2. 在一个循环中，先取出根节点（出队列 + 访问节点）
    3. 把根节点的左右孩子入队列
    然而这里不但要层次遍历，而且要按层输出，于是再增加一个list作为每一层的节点，正好队列的长度就是每一层的元素个数。
    '''

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodeQuene = []
        result = []
        if not root:
            return result
        nodeQuene.append(root)
        while nodeQuene:
            # 这个表示单层节点所有的值
            singleLevel = []
            queneLength = len(nodeQuene)
            for i in range(queneLength):
                currentNode = nodeQuene.pop(0)
                if currentNode.left:
                    nodeQuene.append(currentNode.left)
                if currentNode.right:
                    nodeQuene.append(currentNode.right)
                singleLevel.append(currentNode.val)
            result.append(singleLevel)
        return result

    # 操作给定的二叉树，将其变换为源二叉树的镜像。
    def Mirror(self, root):
        # write code here
        if root is not None:  #根绝ide建议，is not比!= 好
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)


# def preTr(root):
#
#     if root == None:
#         return
#     print root.val
#     preTr(root.left)
#     preTr(root.right)

s = Solution()

# test codes:
# pre = [1, 2, 4, 7, 3, 5, 6, 8]
# tin = [4, 7, 2, 1, 5, 3, 8, 6]
# r = s.reConstructBinaryTree(pre, tin)
# print r.left  # 内存地址 instance：实例
# # s.preTr(r)
# # preTr(r)
# # s.postTr(r)
# s.inTr(r)

a1 = TreeNode(5)
a4 = TreeNode(2)
a5 = TreeNode(3)
a2 = TreeNode(1)
a3 = TreeNode(4)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5

# b1 = TreeNode(1)
# b2 = TreeNode(2)
# b3 = TreeNode(3)
# b1.left = b2
# b1.right = b3

# print a2.right.val == a5.val
# print s.HasSubtree(a1, b2)
# print s.levelOrder(a1)
# print len([a1])
print s.levelOrder(a1)
s.Mirror(a1)
print s.levelOrder(a1)
s.Mirror(None)
print s.levelOrder(None)
