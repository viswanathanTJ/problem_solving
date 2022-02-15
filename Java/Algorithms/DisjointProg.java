import java.io.*;
import java.util.*;
//just do merge
class DisjointProg{
	static int[] parent, rank;
	static int n;
	DisjointProg(int n){
		this.n = n;
		parent = new int[n];
		rank = new int[n];
		makeSet();
	}
	static void makeSet(){
		for(int i=0; i<n; i++)
			parent[i] = i;
	}
	static boolean union(int x, int y){
		int xRoot = find(x);
		int yRoot = find(y);
		if( xRoot == yRoot )
			return false;
		if( rank[xRoot] < rank[yRoot] ){
			parent[xRoot] = yRoot;
		}else if( rank[yRoot] < rank[xRoot] ){
			parent[yRoot] = xRoot;
		}else{
			parent[xRoot] = yRoot;
			rank[xRoot]++;
		}
		return true;
	}
	static int find(int x){
		return parent[x] == x ? parent[x] : find(parent[x]);
	}
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		new DisjointProg(sn.nextInt());
		System.out.println("Union");
		while( true ){
			int s = sn.nextInt();
			int e = sn.nextInt();
			if( s == -1 && e == -1 )
				break;
			System.out.println(union(s, e)==true?"connected":"already connected");
		}
		System.out.println("Find");
		while( true ){
			int s = sn.nextInt();
			int e = sn.nextInt();
			if( s == -1 && e == -1 )
				break;
			System.out.println(find(s)==find(e)?"connected":"not connected");
		}
	}
	static void fill(int[] ar, int n){
		Arrays.fill(ar, n);
	}
}
