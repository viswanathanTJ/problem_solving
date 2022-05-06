public class Permutation {
    static void permute(int a[], int n, int index) {
        for(int i=index; i<n;i++) {
            a[i] = a[i] + a[index] - (a[index] = a[i]);
            permute(a, n, index+1);
            a[index] = a[index] + a[i] - (a[i] = a[i]);
        }
        if(index == n - 1) {
            for(int x: a)
                System.out.print(x + " ");
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int arr[] = {1,2,3};
        permute(arr, 3, 0);
    }
    
}
