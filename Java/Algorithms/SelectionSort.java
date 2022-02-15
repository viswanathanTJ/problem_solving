import java.io.*;
import java.util.*;
public class SelectionSort{
	
	public static final Scanner sn = new Scanner(System.in);
	public static final Random rn = new Random();
	public static final PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) {
		int n = Int();
		int[] ar = new int[n];
		for(int i=0; i<n; i++) ar[i] = Int();
		System.out.println("Sorted Array");
		for(int i=0; i<n; i++){
			int min_index = i;
			for(int j=i+1; j<n; j++){
				if(ar[min_index]>ar[j]){
					min_index = j;
				}
			}
			int t = ar[i];
			ar[i] = ar[min_index];
			ar[min_index] = t;
		}
		for(int x : ar) System.out.print(x+" ");
	}
	public static void fill(int[] ar, int n){
		Arrays.fill(ar, n);
	}
	public static void clearScreen(){
		try{
			new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
		}catch(Exception e){
			System.out.println(e);
		}
	}
	public static int Int(){
		return sn.nextInt();
	}
	public static long getMS(){
		return System.currentTimeMillis();
	}
	public static char[] chararr(String s){
		return s.toCharArray();
	}
}
