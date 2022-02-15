import java.io.*;
import java.util.*;
class QuickSort{
	public static void sort(int[] ar, int start, int end){
		if( start < end ){
			int pind = partition(ar, start, end);
			sort(ar, start, pind-1);
			sort(ar, pind+1, end);
		}
	}
	public static int partition(int[] ar, int s, int e){
		int pivot  = ar[e];
		int pind = s;
		for(int i=s; i<e; i++){
			if( ar[i] <= pivot ){
				int t = ar[i];
				ar[i] = ar[pind];
				ar[pind] = t;
				pind++;
			}
		}
		int t = ar[e];
		ar[e] = ar[pind];
		ar[pind] = t;
		return pind;
	}
	public static final Scanner sn = new Scanner(System.in);
	public static final Random rn = new Random();
	public static void main(String[] args) {
		System.out.println("Enter array size : ");
		int n = Int();
		int[] arr = new int[n];
		System.out.println("Enter Array Elements : ");
		for(int i=0; i<n; i++) arr[i] = Int();
		sort(arr, 0, arr.length-1);
		System.out.println("Sorted Array : ");
		for(int x : arr) System.out.print(x+" ");
	}
	public static int Int(){
		return sn.nextInt();
	}
}