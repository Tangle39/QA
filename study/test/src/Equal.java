public class Equal {
    public static void main(String[] args) {


        String a = "1234";
        String b = "1234";
        String c = new String("1234");
        System.out.println(a == b); //true
        System.out.println(a == c);//false
        System.out.println(a.equals(c));//true
    }

}
/*
第一次String a="1234"时，会在常量池中创建一个常量1234,String b=1234时，
常量池中已经有了该常量，所以直接取，a和b的地址一样，所以地址值相等；
String c = newString("1234")重新new了对象，在堆内存中开辟了新的空间，所以地址值不想等，
而equals方法比较的是值是否相等

* */