import java.util.Stack;
//用栈实现队列
public class Solution {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int node) {
        stack1.push(node);
    }

    public int pop() {
        if(stack1.empty()&&stack2.empty()){
            throw new RuntimeException("Queue is empty!");
        }
        if(stack2.empty()){
            while(!stack1.empty()){
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
    public static void main(String[] args)
    {
        System.out.println("Hello World");
        //Stack<Integer> s = new Stack<Integer>();
        Solution s1 = new Solution();

        s1.push(4);
        s1.push(5);
        s1.push(6);

        System.out.println(s1.pop());
    }
}