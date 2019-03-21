//
//  main.cpp
//  Stu
//
//  Created by なな on 2019/3/17.
//  Copyright © 2019 なな. All rights reserved.
//

#include <iostream>
using namespace std;

//使用泛型类型定义函数，称为函数模板
template <class T>
T sum(T a,T b)
{
    T result;
    result = a+b;
    return result;
}
void f1()
{
    int i =5,j=6,k;
    double f=2.0,g=0.5,h;
    k=sum(i, j);//k=sum<int>(i, j);
    h=sum(f, g);
    
    cout<<k<< '\n';
    cout<<h<< '\n';
}
int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    f1();
    return 0;
}
