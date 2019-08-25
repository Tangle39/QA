#滑动窗口
#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
def lengthOfLongestSubstring(s: str) -> int:
    if not s:return 0
    left = 0
    lookup =set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])   #集合移除元素，不存在会报错
            left +=1
            cur_len -= 1
        if cur_len > max_len: max_len = cur_len
        lookup.add(s[i])
    return max_len
print(lengthOfLongestSubstring('abcdd'))