#-*-coding: UTF-8-*-
'''
一个字符串中，某一个子串它的下标，如果有，则返回这个子串首次出现的下标，如果没有，就返回-1
'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        num = len(needle)
        if len(haystack) < num:
            return -1
        elif haystack == "" and needle == "":
            return 0
        else:
            for i in range(len(haystack)):#0 1 2 3 4
                if(haystack[i:num+i]==needle):#[0:2] 简单暴力，这样子格式可以
                    return i
        return -1
if __name__ == '__main__':
    S = Solution()
    h = ("hello")
    n = ("lo")

    print(S.strStr(h,n))

'''
---------------------

原文：https://blog.csdn.net/qq_36470920/article/details/84963905
'''
