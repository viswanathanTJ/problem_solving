import java.util.Scanner;

public class Queue {
    static int n = 5, f = 0, r = 0;
    static int queue[] = new int[50];
    static void enque(int val) {
        if(r == n - 1) System.out.println("Queue is full");
        else
            queue[r++] = val;
    }
    static void deque() {
        if(f==-1) System.out.println("Queue is empty");
        else
            System.out.println("Dequed element is " + queue[f++]);
    }
    static void print() {
        for(int i=f; i<r;i++)
            System.out.print(queue[i]+" ");
    }
    

    public static void main(String[] args) {
        int ch = 1, n;
        Scanner sc = new Scanner(System.in);
        while(true) {
            System.out.println("1.Enque\n2.Deque\n3.Print\n0.Exit\nEnter you choice: ");
            ch = sc.nextInt();
            if(ch == 0) break;
            switch(ch) {
                case 1:
                    System.out.println("Enter value to enque: ");
                    n = sc.nextInt();
                    enque(n);
                    break;
                case 2:
                    deque();
                    break;
                case 3:
                    print();
                    System.out.println();
                    break;
                default:
                    System.out.println("Invalid input");
            }
            
        }
        sc.close();
    }
}
