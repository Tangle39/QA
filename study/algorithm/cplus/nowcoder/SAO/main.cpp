//
//  main.cpp
//  SAO
//
//  Created by なな on 2017/10/12.
//  Copyright © 2017年 なな. All rights reserved.
//  command + R编译

#include "dataStruct.hpp"
/*把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。*/
//二分查找的变形
/*二分查找：
 int binary_search(int arr[], int n, int key)
{
    int left = 0;   //数组的首位置，即arr[0]处
    int right = n - 1;//数组的最后一个位置，即arr[n-1],数组大小为n
    
    //循环条件一定要注意
    while (left <= right)
    {
        int mid = left + ((right - left) >> 1);//此处的mid的计算一定要放在while循环内部，否则mid无法正确更新;并且此处用移位代替除以2可以提高效率，而且可以防止溢出。
        if (arr[mid] > key)//数组中间的位置得数大于要查找的数，那么我们就在中间数的左区间找
        {
            right = mid - 1;
        }
        else if (arr[mid] < key)//数组中间的位置得数小于要查找的数，那么我们就在中间数的右区间找
        {
            left = mid + 1;
        }
        else
        {
            return mid;//中间数刚好是要查找的数字。
        }
    }
    
    //执行流如果走到此处说明没有找到要查找的数字。
    return -1;
}
 */
// 顺序寻找最小值

int MinOrder(vector<int> &num,int left,int right){
    int result = num[left];
    for(int i = left + 1;i < right;++i){
        if(num[i] < result){
            result = num[i];
        }//if
    }//for
    return result;
}
int minNumberInRotateArray(vector<int> rotateArray)
{
   
    int size = rotateArray.size();
    if(size == 0){
        return 0;
    }//if
    int left = 0,right = size - 1;
    int mid = 0;
   
    while(rotateArray[left] >= rotateArray[right]){
        // 分界点
        if(right - left == 1){
            mid = right;
            break;   //退出循环
        }//if
        mid = left + (right - left) / 2;
        // rotateArray[left] rotateArray[right] rotateArray[mid]三者相等
        // 无法确定中间元素是属于前面还是后面的递增子数组
        // 只能顺序查找
        if(rotateArray[left] == rotateArray[right] && rotateArray[left] == rotateArray[mid]){
            return MinOrder(rotateArray,left,right);//数组有重复数字，形如测试用例
        }//if
        // 中间元素位于前面的递增子数组
        // 此时最小元素位于中间元素的后面
        if(rotateArray[mid] >= rotateArray[left]){
            left = mid;
        }//if
        // 中间元素位于后面的递增子数组
        // 此时最小元素位于中间元素的前面   test
        else{
            right = mid;
        }//else
    }//while
    return rotateArray[mid];
}

int main(int argc, char* argv[])
{
   vector<int> num = {2,2,2,2,1,2};
    int res=minNumberInRotateArray(num);
    cout<<res<<endl;
    cout<<"sakupopo";
    return 0;
}


