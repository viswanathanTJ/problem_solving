import java.util.Scanner;


class MyStack {
    int top = -1;
    int n;
    int arr[] = new int[50];

    MyStack(int n) {
        this.n = n;
    }

    void push(int val) {
        if(top == n - 1) System.out.println("Stack is full");
        else
            arr[++top] = val;
    }

    void pop() {
        if(top == -1) System.out.println("Stack is empty");
        else 
            System.out.println(arr[top--] + " is popped");
    }

    void display() {
        if(top != -1)
            for(int i=0;i<=top;i++)
                System.out.print(arr[i]+" ");
    }
}

public class Stack {
    public static void main(String[] args) {
        int ch = 1, n;
        Scanner sc = new Scanner(System.in);
        MyStack s = new MyStack(5);
        while(ch != 0) {
            System.out.println("1.Push\n2.Pop\n3.Display\n0.Exit\nEnter you choice: ");
            ch = sc.nextInt();
            if(ch == 0) break;
            switch(ch) {
                case 1:
                    System.out.println("Enter value to push: ");
                    n = sc.nextInt();
                    s.push(n);
                    break;
                case 2:
                    s.pop();
                    break;
                case 3:
                    s.display();
                    System.out.println();
                    break;
                default:
                    System.out.println("Invalid input");
            }
            
        }
        sc.close();
    }
}
