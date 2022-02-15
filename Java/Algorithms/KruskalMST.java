import java.io.*;
import java.util.*;
class KruskalMST{
	public int V, E;
	class subsets{
		int parent, rank;
	}
	class Edge implements Comparable<Edge>{
		int source, destination, weight;
		public int compareTo(Edge edge){
			return this.weight - edge.weight;
		}
	}
	Edge[] edge;
	KruskalMST(int V, int E){
		this.V = V;
		this.E = E;
		edge = new Edge[E];
		for(int i=0; i<E; i++)
			edge[i] = new Edge();
	}
	public int find(subsets[] subset, int x){
		return x == subset[x].parent ? x : find(subset, subset[x].parent);
	}
	public void union(subsets[] subset, int x, int y){
		if( subset[x].rank < subset[y].rank ){
			subset[x].parent = y;
		}else if( subset[y].rank < subset[y].rank ){
			subset[y].parent = x;
		}else{
			subset[y].parent = x;
			subset[y].rank++;
		}
	}
	public void MST(){
		Edge[] result = new Edge[V];
		for(int i=0; i<V; i++)
			result[i] = new Edge();
		subsets[] subset = new subsets[V];
		for(int i=0; i<V; i++)
			subset[i] = new subsets();
		for(int i=0; i<V; i++){
			subset[i].parent = i;
			subset[i].rank = 0;
		}
		Arrays.sort(edge);
		int i=0, e=0;
		while( e < V-1 ){
			Edge nextEdge = edge[i++];
			int x = find(subset, nextEdge.source);
			int y = find(subset, nextEdge.destination);
			if( x != y ){
				result[e++] = nextEdge;
				union(subset, x, y);
			}
		}
		int tot = 0;
		for(i=0; i<e; i++){
			System.out.println(result[i].source+" -- "+result[i].weight+" -- "+result[i].destination);
			tot += result[i].weight;
		}
		System.out.println(tot);
	}
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		System.out.println("Enter the Number of Vertices and Edges :");
		KruskalMST k = new KruskalMST(sn.nextInt(), sn.nextInt());
		System.out.println("Enter source , weight and destination : ");
		for(int i=0; i<k.E; i++){
			k.edge[i].source = sn.nextInt();
			k.edge[i].destination = sn.nextInt();
			k.edge[i].weight = sn.nextInt();
		}
		k.MST();
	}
	static void fill(int[] ar, int n){
		Arrays.fill(ar, n);
	}
}