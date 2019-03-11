
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        //指定200元的金额
        test2(200);
        long endTime = System.currentTimeMillis();
        System.out.println("执行时间：" + (endTime - startTime) + "ms");
    }

}


