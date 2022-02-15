import java.io.*;
import java.util.*;
class SetMatricsZero{
	
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		
	}
	static ArrayList<Integer> list(){
		return new ArrayList<Integer>();
	}
	static HashSet<Integer> set(){
		return new HashSet<Integer>();
	}
	static void fill(int[] ar, int n){
		Arrays.fill(ar, n);
	}
	static void clearScreen(){
		try{
			new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
		}catch(Exception e){
			System.out.println(e);
		}
	}
	static char[] chararr(String s){
		return s.toCharArray();
	}
}
