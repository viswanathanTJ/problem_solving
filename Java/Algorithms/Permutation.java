import java.io.*;
import java.util.*;
public class Permutation{
	public static void permute( int[] arr, int n, int index ){
		for(int i=index; i<n; i++){
			swap(arr, i, index);
			permute(arr, n, index+1);
			swap(arr, index, i);
		}
		if( index == n-1 ){
			System.out.print("[ ");
			for(int x : arr) System.out.print(x+" ");
			System.out.println("]");
		}
	}
	public static void swap(int[] arr, int i, int j){
		int t = arr[i];
		arr[i] = arr[j];
		arr[j] = t;
	}
	public static final Scanner sn = new Scanner(System.in);
	public static final Random rn = new Random();
	public static final PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) {
		int n = Int();
		int[] arr = new int[n];
		for(int i=1; i<=n; i++) arr[i-1] = i;
		permute(arr, n, 0);
		for(int x : arr) System.out.print(x+" ");
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
	public static char[] chararr(String s){
		return s.toCharArray();
	}
	public static int Int(){
		return sn.nextInt();
	}
	public static char Char(){
		return sn.next().charAt(0);
	}
	public static double Double(){
		return sn.nextDouble();
	}
	public static float Float(){
		return sn.nextFloat();
	}
	public static long Long(){
		return sn.nextLong();
	}
}
