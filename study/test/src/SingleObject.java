/*
设计模式（Design pattern）代表了最佳的实践，通常被有经验的面向对象的软件开发人员所采用。
单例模式（Singleton Pattern）是 Java 中最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。
这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。
1、单例类只能有一个实例。
2、单例类必须自己创建自己的唯一实例。
3、单例类必须给所有其他对象提供这一实例。
*/
public class SingleObject {

    //创建 SingleObject 的一个对象
    private static SingleObject instance = new SingleObject();
    //static:方便在没有创建对象的情况下来进行调用（方法/变量）。

    //让构造函数为 private，这样该类就不会被实例化
    private SingleObject(){}

    //获取唯一可用的对象
    public static SingleObject getInstance(){
        return instance;
    }

    public void showMessage(){
        System.out.println("Offer comes soon!");
    }
}
