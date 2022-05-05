import java.util.Scanner;


class LinkedList {
    static class Node {
        int val;
        Node next;
        Node(int n) {
            val = n;
            next = null;
        }
    }
    public static Node add(Node head, int n) {
        if(head == null) return new Node(n);
        Node temp = head;
        while(temp.next != null)
            temp = temp.next;
        Node newNode = new Node(n);
        temp.next = newNode;
        return head;
    }
    public static Node remove(Node head) {
        if(head == null) return head;
        Node temp = head;
        System.out.println("Removed "+temp.val);
        return temp.next;
    }
    public static void print(Node head) {
        Node temp = head;
        while(temp != null) {
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int ch = 1, n;
        Node head = null;
        Scanner sc = new Scanner(System.in);
        while(true) {
            System.out.println("1.Add\n2.Remove\n3.Print\n0.Exit\nEnter you choice: ");
            ch = sc.nextInt();
            if(ch == 0) break;
            switch(ch) {
                case 1:
                    System.out.println("Enter value to add: ");
                    n = sc.nextInt();
                    head = add(head, n);
                    break;
                case 2:
                    head = remove(head);
                    break;
                case 3:
                    print(head);
                    System.out.println();
                    break;
                default:
                    System.out.println("Invalid input");
            }
            
        }
        sc.close();
    }
}