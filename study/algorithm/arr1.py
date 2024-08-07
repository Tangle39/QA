# -*- coding:utf-8 -*-
class Solution:
    """
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
    """

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)  # +=和append的差异
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat


s = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.printMatrix(mat))
