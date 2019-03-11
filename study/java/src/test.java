
public class test {

    /**
     * @param x 商品金额
     */
    public static void test2(int n) {
        //纸币面额
        int money[] = {1, 5, 10, 20, 50, 100};
        int dp[] = new int[n + 1];
        dp[0] = 1;
        for (int i = 0; i < 6; ++i) {
            for (int j = money[i]; j <= n; ++j) {
                dp[j] = (dp[j] + dp[j - money[i]]);
            }
        }
        System.out.println(dp[n]);
    }

}
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        //指定200元的金额
        test2(200);
        long endTime = System.currentTimeMillis();
        System.out.println("执行时间：" + (endTime - startTime) + "ms");
    }

}