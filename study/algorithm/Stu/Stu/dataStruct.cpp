//
//  dataStruct.cpp
//  SAO
//
//  Created by なな on 2017/10/26.
//  Copyright © 2017年 なな. All rights reserved.
//

#include "dataStruct.hpp"
int FirstNotRepeatingChar(string str) {
    map<char, int> mp;
    for(int i = 0; i < str.size(); ++i)
        mp[str[i]]++;
    for(int i = 0; i < str.size(); ++i){
        if(mp[str[i]]==1)
            return i;
    }
    return -1;
}
//so difficult https://www.nowcoder.com/profile/9621645/codeBookDetail?submissionId=17505991
long InversePairsCore( vector<int> &data, vector<int> &copy, long start, long end){
    if(start == end)  // copy: 辅助数组
    {
        return 0 ;  // 递归终止条件
    }
    
    long length = (end-start)/ 2 ;
    long left = InversePairsCore(copy,data, start, start+length); // 递归，归并排序，并计算本次逆序对数
    long right = InversePairsCore(copy,data, start+length+1, end);
    long crossCount = 0 ;       // 记录交叉的逆序对数
    long i = (start+length), j = end, temp = end;  //i：前半部分的下标，j：后半部分的下标，temp：辅助数组的下标
    
    while(i >= start && j >= start+length+1) {   // 存在交叉的逆序对，先统计一下，然后依次将较大值放进辅助数组
        if (data[i] > data[j]) {
            copy[temp--] = data[i--];
            crossCount += j - start - length;
        } else {
            copy[temp--] = data[j--];   // 不存在交叉的逆序对，依次将较大值放进辅助数组
        }
    }
    while(i >= start) {
        copy[temp--] = data[i--];
    }
    while(j >=start+length+1) {
        copy[temp--] = data[j--];
    }
    return (left + right + crossCount) % 1000000007; //数值过大时求余, 防止溢出
}
int InversePairs(vector<int> &data) {
    if(data. size () == 0 ) return 0 ;
    else if (data. size() == 1 ) return 1 ;
    else {
        vector<int> copy(data);
        return InversePairsCore(copy, data, 0 , data.size()- 1);
    }
}
ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2)
{
    ListNode *p1 = pHead1;
    ListNode *p2 = pHead2;
    while(p1!=p2)
    {
        p1 = (p1==NULL ? pHead2 : p1->next);
        p2 = (p2==NULL ? pHead1 : p2->next);
}

return p1;
}
bool IsBalanced(TreeNode *proot)
{
    if (proot==NULL)
    {
        return true;
    }
    int leftDepth=getDepth(proot->left);
    int rightDepth=getDepth(proot->right);
    if(leftDepth>rightDepth+1||rightDepth>leftDepth+1)
        return false;
    else
        return IsBalanced(proot->left)&&IsBalanced(proot->right);
}
int getDepth(TreeNode *proot){
    if (proot==NULL) {
        return 0;
    }
        int leftDepth=getDepth(proot->left);
        int rightDepth=getDepth(proot->right);
    return leftDepth>rightDepth?leftDepth+1:rightDepth+1;
}
vector<vector<int>> FindContinuousSeq(int sum){
    int l=1;int r=1;int sumx=1;//用sumx来逼近、判断sum，从1开始 lr为左右两侧
    vector<vector<int>> ans;
    while (l<=r) {//循环出口
        r++;
        sumx+=r;
        while(sumx>sum){
            sumx-=l;
            l++;   //若sumx超了，从左边减去l；同时l++保证了r到达sum时的出口
        }
        if (sumx==sum&&l!=r) {
            vector<int> tmp;
            for (int i=l; i<=r; i++) {
                tmp.push_back(i);//发现答案时存入tmp
            }
                ans.push_back(tmp);
        }
    }
    return ans;
}
vector<int> FindNumWithSum(vector<int> array,int sum){
    vector<int> res;
    int i=0,j=array.size()-1;
    while (i<j) {
        if (array[i]+array[j]==sum) {
            res.push_back(array[i]);
            res.push_back(array[j]);
            break;
        }
        while (array[i]+array[j]>sum) {
            j--;
        }
        while (array[i]+array[j]<sum) {
            i++;
        }
    }
    return res;
}
string LeftRotateString(string str, int n)
{   int k=n%str.length();
    
    if (k==0) {
        return str;
    }
    string res=str.substr(0,k);//str.substr(pos, n) 返回一个字符串，包含s中从下标pos开始的n个字符
    str.erase(0,k);
    str+=res;
    return str;
}
/*顺子满足的条件：max-min<5;
 除0外其他的数字都不能重复
*/
bool IsContinuous(vector<int> numbers){
    if (numbers.empty()) {
        return 0;
    }
    int count[14]={0};//记录每个元素出现的次数;以numbers中的元素作为下标(最大K,对应13)
    int min=13;
    int max=0;
    for (int i=0; i<numbers.size(); i++) {
        count[numbers[i]]++;
        if (numbers[i]==0) {
            continue;//因为有1个以上0是没关系的
        }
        if (count[numbers[i]]>1) {
            return 0;
        }
        if (numbers[i]>=max) {
            max=numbers[i];
        }
        if (numbers[i]<=min) {
            min=numbers[i];
        }
    }
    if (max-min<5) {
        return 1;
    }
    return 0;
}
//列表通常在容器中已获得迭代器的任意位置处插入、获得（Extracting，提取）、移动元素等操作中表现出更出色的性能，
int JosefProblem(int n,int m){
    list<int> circle;//初始化
    for (int i=1; i<=n; i++) {
        circle.push_back(i);
    }
    list<int>::iterator cur=circle.begin();//迭代器
    while (circle.size()>1) {
        //数到m的人出局
        for (int i=0; i<m-1; i++) {
            cur++;
            if (cur==circle.end()) {
                cur=circle.begin();//到尾的话改到头部
            }
        }
            //删除数到m的人，先记录下一个人的地址，再cur回退，到尾的话，回到头部
            list<int>::iterator next=++cur;  //注意i++与++
        if (next==circle.end()) {
            next=circle.begin();
        }
        cur--;
        circle.erase(cur);
        cur=next;
    }
    return circle.front();
}
int sum_solution(int n){
    bool a[n][n+1];//bool型sizeof为1
    return sizeof(a)>>1;//右移1相当于除以2
}
int sum_solution2(int n){
    /*利用逻辑与的短路特性实现递归终止。*/
    int ans = n;
    ans&&(ans+=sum_solution2(n-1));
    return ans;
}
bool duplicate(int numbers[], int length, int* duplication) {
    if(numbers==NULL||length==0) return 0;
    int hashTable[255]={0};
    for(int i=0;i<length;i++)
    {
        hashTable[numbers[i]]++;
    }
    int count=0;
    for(int i=0;i<length;i++)
    {
        if(hashTable[numbers[i]]>1)
        {
            duplication[count++]=numbers[i];
            //break;
            return true;
        }
    }
    return false;
}
/* 【构建成绩数组】 page 3 剑指offer from牛客网
 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
 解：
 B[i]的值可以看做矩阵中每行的乘积
 [1 A1 A2...An-2 An-1
  A0 1 A2...An-1 An-1
  A0 A1 1...An-2 An-1
 ...
  A0 A1...An-3 An-2 1]
 
 */
vector<int> multiply(const vector<int>& A){
    int n=A.size();
    vector<int> B(n,1);  //初始化为n个1
    vector<int> B0(n,1);
    vector<int> B1(n,1);
    for (int i=1; i<n; i++) {
        B0[i]=B0[i-1]*A[i-1];
    }//下三角
    for (int i=n-2; i>=0; i--) {
        B1[i]=B1[i+1]*A[i+1];
    }//上三角
    for (int i=0; i<n; i++) {
        B[i]=B0[i]*B1[i];
    }
    return B;
}
/*
 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
 而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
 
 */
bool match(char* str, char* pattern)
{
    if (pattern[0] == 0 && str[0] == 0)//两个均为空串;递归出口（匹配的话,会不断移位至两个都为空串）
    {
        return true;
    }
    
    if (pattern[1] == '*')
    {
        if (match(str, pattern + 2))//若pattern第二位为*，*能匹配两位，则相当于str于pattern+2匹配 eg null,q*
            return true;
    }
    
    if ((pattern[0] == '.' && str[0]) || str[0] == pattern[0]) //如果pattern第一位为0/两个串首字符相同
    {
        if (match(str + 1, pattern + 1))  //相当于都后移1位再匹配
            return true;
        if (pattern[1] == '*' && match(str + 1, pattern))  //若后移一位首字母不同，但是pattern为*，则相当于str后移一位再与pattern匹配
        {
            return true;
        }
    }
    
    return false;
}
