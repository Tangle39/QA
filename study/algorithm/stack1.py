# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # stack中存入pushV中取出的数据
        stack = []
        while popV:
            # 如果第一个元素相等，直接都弹出，根本不用压入stack
            if pushV and popV[0] == pushV[0]:
                popV.pop(0)
                pushV.pop(0)
            # 如果stack的最后一个元素与popV中第一个元素相等，将两个元素都弹出
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            # 如果pushV中有数据，压入stack
            elif pushV:
                stack.append(pushV.pop(0))
            # 上面情况都不满足，直接返回false。
            else:
                return False
        return True


s = Solution()
p1 = [1,2,3,4,5]
p2 = [1,2,5,4,3]
print s.IsPopOrder(p1,p2)