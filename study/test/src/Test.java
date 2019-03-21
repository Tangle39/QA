public class Test{

    public static void main(String args[]){
        Integer x = 5;
        x =  x + 10;
        System.out.println(x);
    }
}
//当 x 被赋为整型值时，由于x是一个对象，所以编译器要对x进行装箱。
// 然后，为了使x能进行加运算，所以要对x进行拆箱。