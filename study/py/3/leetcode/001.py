# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}  # 字典
        res = []
        for index, value in enumerate(nums): #可以用它list（enumerate（t))打印
            data[value] = index  #存字典
            if target - value in data:  # 利用字典以及enumerate巧妙得出res ；字典只有key做判断
                res.append([data[target - value], index])  # 重复的也能统计
        return res

    def twoSum2(self, nums, target):
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return "No solution here!"
            r = target - nums[i]
            # Can't use a num twice
            num_follow = nums[i + 1:]
            if r in num_follow:
                return [i, num_follow.index(r) + i + 1]
            i = i + 1


s = Solution()

print(s.twoSum([2, 7, 1, 2, 7, 4], 9))
print(s.twoSum2([2, 7, 1, 2, 7, 4], 9))
