import java.util.*;

class Soln {
    public static void permute(int[] arr, int n, int index) {
        for (int i = index; i < n; i++) {
            swap(arr, i, index);
            permute(arr, n, index + 1);
            swap(arr, index, i);
        }
        if (index == n - 1) {
            for (int x : arr)
                System.out.print(x + " ");
            System.out.println();
        }
    }

    public static void swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args) {
        int n = 5;
        int[] arr = new int[n];
        for (int i = 1; i <= n; i++)
            arr[i - 1] = i;
        permute(arr, n, 2);
    }
}