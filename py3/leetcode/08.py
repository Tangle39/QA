import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)  # lstrip() 去除左边的空格
# ^匹配开头 +一个或多个  ？0次或1次（前面的) 利用了max和min   *解包 \避免歧义


s = Solution()
print(s.myAtoi('words42trd'))


