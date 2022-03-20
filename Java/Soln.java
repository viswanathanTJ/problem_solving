import java.util.*;

class Soln {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        while (q-- != 0) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            int x = sc.nextInt();
            for (int i = l - 1; i < r; i++)
                a[i] &= x;
        }
        for (int i : a)
            System.out.print(i + " ");
    }
}