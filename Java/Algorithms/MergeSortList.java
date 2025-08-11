import java.util.*;
class node {
    int val;
    node next;

    node(int val) {
        this.val = val;
        this.next = null;
    }
}
public class MergeSortList {

    static node push(node head, int val) {
        if (head == null)
            return new node(val);
        else {
            node n = new node(val);
            n.next = head;
            return n;
        }
    }

    static void print(node head) {
        node cur = head;
        while (cur != null) {
            System.out.print(cur.val + " ");
            cur = cur.next;
        }
    }

    static node get_mid(node head) {
        node slow = head;
        node fast = head;
        node prev = null;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        return prev;
    }

    static node merge(node left, node right) {
        node dummy = new node(-1);
        node temp = dummy;
        while (left != null && right != null) {
            if (left.val < right.val) {
                temp.next = left;
                left = left.next;
            } else {
                temp.next = right;
                right = right.next;
            }
            temp = temp.next;
        }
        if (left != null)
            temp.next = left;
        if (right != null)
            temp.next = right;
        return dummy.next;
    }

    static node mergeSort(node head) {
        if (head == null || head.next == null)
            return head;
        node left = head;
        node mid = get_mid(head);
        node right = mid.next;
        mid.next = null;
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }

    public static void main(String[] args) {
        node head = new node(5);
        Random rn = new Random();
        for (int i = 0; i < 5; i++)
            head = push(head, rn.nextInt(50));
        print(head);
        head = mergeSort(head);
        System.out.println();
        print(head);
    }
}
