import java.io.*;
import java.util.*;
public class BogoSort{
	public static boolean isSorted( List<Integer> list ){
		int prev = list.get(0);
		for(int x : list){
			if(prev>x) return false;
			prev = x;
		}
		return true;
	}
	public static final Scanner sn = new Scanner(System.in);
	public static final Random rn = new Random();
	public static final PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) {
		List<Integer> list = new ArrayList();
		int n = Int();
		for(int i=0; i<n; i++)list.add(sn.nextInt());
		while(!isSorted(list)) Collections.shuffle(list);
		System.out.println("sorted");
		list.forEach(i->System.out.println(i));
	}
	public static int Int(){
		return sn.nextInt();
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
}
