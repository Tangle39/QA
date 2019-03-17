//
//  dataStruct.hpp
//  SAO
//
//  Created by なな on 2017/10/26.
//  Copyright © 2017年 なな. All rights reserved.
//
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <list>
#include <algorithm>
#include <stack>
using namespace std;
#ifndef dataStruct_hpp
#define dataStruct_hpp

#include <stdio.h>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) :val(x), next(NULL) {}
};
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) :val(x),left(NULL),right(NULL){}
};

int FirstNotRepeatingChar(string str);
long InversePairsCore(vector<int> &data, vector<int> &copy, long start, long end);
int InversePairs(vector<int> &data);
ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2);
bool IsBalanced(TreeNode *proot);
int getDepth(TreeNode *proot);
vector<vector<int>> FindContinuousSeq(int sum);
vector<int> FindNumWithSum(vector<int> array,int sum);
string LeftRotateString(string str, int n);
bool IsContinuous(vector<int> numbers);
int JosefProblem(int n,int m);
int sum_solution(int n);
int sum_solution2(int n);
bool duplicate(int numbers[], int length, int* duplication);
vector<int> multiply(const vector<int>& A);
bool match(char* str, char* pattern);
#endif /* dataStruct_hpp */
