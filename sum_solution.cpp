//求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
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