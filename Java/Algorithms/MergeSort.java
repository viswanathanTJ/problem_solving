import java.io.*;
import java.util.*;
class MergeSort{
	public static final Scanner sn = new Scanner(System.in);
	public static final Random rn = new Random();
	public static void sort(int[] arr){
		int n = arr.length;
		if( n < 2 )
			return;
		int mid = n / 2;
		int[] l = new int[mid];
		int[] r = new int[n-mid];
		for(int i=0;i<mid;i++)
			l[i] = arr[i];
		for(int i=mid;i<n;i++)
			r[i-mid] = arr[i];
		sort(l);
		sort(r);
		merge(l,r,arr);
	}
	public static void merge(int[] l, int[] r, int[] arr){
		int i = 0, j = 0, k = 0, nl = l.length, nr = r.length;
		while( i < nl && j < nr ){
			if( l[i] <= r[j] ){
				arr[k] = l[i];
				i++;
			}else{
				arr[k] = r[j];
				j++;
			}
			k++;
		}
		while( i < nl ){
			arr[k++] = l[i++];
		}
		while( j < nr ){
			arr[k++] = r[j++];
		}
	}
	public static void main(String[] args) {
		System.out.print("Enter array size : ");
		int n = sn.nextInt();
		int[] arr = new int[n];
		int i = 0;
		System.out.println();
		System.out.print("Generated Elements : ");
		while( n-- > 0 ){
			int val = rn.nextInt(1000);
			arr[i++] = val;
			System.out.print(val+" ");
		}
		System.out.println();
		System.out.println();
		System.out.print("Sorted Elements are : ");
		sort(arr);
		for(int x : arr)
			System.out.print(x+" ");
	}
}