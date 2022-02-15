import java.io.*;
import java.util.*;
class NumberOfIslands{
	public static int dfs(int[][] mat){
		int n = mat.length;
		boolean[][] visit = new boolean[n][n];
		for(int i=0; i<n; i++)
			Arrays.fill(visit[i], false);
		int count = 0;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if( !visit[i][j] && mat[i][j] == 1 ){
					dfs(i, j, mat, visit);
					count++;
				}
			}
		}
		return count;
	}
	public static void dfs(int i, int j, int[][] mat, boolean[][] visit){
		if( i < 0 || j < 0 || i >= mat.length || j >= mat.length || visit[i][j] || mat[i][j] == 0 )
			return;
		visit[i][j] = true;
		dfs(i+1, j, mat, visit);
		dfs(i-1, j, mat, visit);
		dfs(i, j+1, mat, visit);
		dfs(i, j-1, mat, visit);
	}
	public static int bfs(int[][] mat){
		int n = mat.length;
		boolean[][] visit = new boolean[n][n];
		for(int i=0; i<n; i++)
			Arrays.fill(visit[i], false);
		int[][] dirs = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
		int count = 0;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if( !visit[i][j] && mat[i][j] == 1 ){
					Queue<int[]> q = new LinkedList<>();
					q.add(new int[]{i, j});
					visit[i][j] = true;
					count++;
					while( !q.isEmpty() ){
						int[] pair = q.poll();
						for(int[] dir : dirs){
							int ii = dir[0] + pair[0];
							int jj = dir[1] + pair[1];
							if( ii >= 0 && jj >= 0 && ii < n && jj < n && mat[ii][jj] == 1 && !visit[ii][jj] ){
								q.add(new int[]{ii, jj});
								visit[ii][jj] = true;
							}
						}
					}
				}
			}
		}
		return count;
	}
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		int n = sn.nextInt();
		int[][] mat = new int[n][n];
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				mat[i][j] = rn.nextInt(2);
				System.out.print(mat[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println("DFS : "+dfs(mat));
		System.out.println("BFS : "+bfs(mat));
	}
	static void fill(int[] ar, int n){
		Arrays.fill(ar, n);
	}
	static char[] chararr(String s){
		return s.toCharArray();
	}
}
