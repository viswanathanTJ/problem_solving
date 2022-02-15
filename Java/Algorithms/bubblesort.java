import java.io.*;
import java.util.*;
class bubblesort{
	public static final Scanner sn = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.println("enter size : ");
		int n = sn.nextInt();
		System.out.println("enter elements : ");
		int[] arr = new int[n];
		for(int i=0;i<n;i++){
			arr[i] = sn.nextInt();
		}
		System.out.println("elements are : ");
		print(arr);
		System.out.println();
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if( arr[i] > arr[j] ){
					int t = arr[i];
					arr[i] = arr[j];
					arr[j] = t;
				}
			}
		}
		System.out.println("sorted elements are : ");
		print(arr);
	}
	static void print(int[] arr){
		for(int x : arr)
			System.out.print(x + " ");
	}
}