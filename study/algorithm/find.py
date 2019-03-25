# encoding:utf-8
#把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


def minNumberInRotateArray(rotateArray):
    # write code here
    pre = -7e20
    for num in rotateArray:   #即min(array)
        if num < pre:
            return num
        pre = num

    if len(rotateArray) == 0:
        return 0
    return rotateArray[0]  #等值数列
#二分法
class Solution:
    def minNumberInRotateArray2(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        low =0
        high = len(rotateArray)-1
        while low<high:
            mid = low + (high - low)/2
            if rotateArray[mid]>rotateArray[high]:
                low = mid+1
            elif rotateArray[mid]==rotateArray[high]:
                high =high-1
            else:
                high = mid
        return rotateArray[low]

r = [1,2,3,4,5,5]
s=Solution()
print s.minNumberInRotateArray2(r)