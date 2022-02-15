import java.io.*;
import java.util.*;
/*
up 24, 30
down 25, 31
left 27, 17
right 26, 16
box - 127
*/
class Maze{
	public void dfs(char[][] maze, int i, int j, int e, boolean[][] visit, char ch){
		if( i == e-1 && j == e-1 && maze[i][j] == '@' ){
			System.out.println("Path Exist");
			System.exit(0);
		}
		if( i >=0 && j >= 0 && i < e && j < e && maze[i][j] == '.' && !visit[i][j] ){
			try{
				clearScreen();
				Thread.sleep(0);
			}catch(Exception ee){
				System.out.println(ee);
			}
			maze[i][j] = ch;
			print(maze);
			maze[i][j] = '.';
			visit[i][j] = true;
			dfs(maze, i+1, j, e, visit, (char)31);
			dfs(maze, i-1, j, e, visit, (char)30);
			dfs(maze, i, j+1, e, visit, (char)16);
			dfs(maze, i, j-1, e, visit, (char)17);
			/*dfs(maze, i-1, j-1, e, visit, (char)17);
			dfs(maze, i+1, j+1, e, visit, (char)17);
			dfs(maze, i+1, j-1, e, visit, (char)17);
			dfs(maze, i-1, j+1, e, visit, (char)17);*/
			//maze[i][j] = ' ';
		}
	}
	public void print(char[][] maze){
		for(char[] ar : maze){
			for(char ch : ar)
				System.out.print(ch+" ");
			System.out.println();
		}
	}
	public void bfs(char[][] maze, int x, int y){
		int n = maze.length;
		boolean[][] visit = new boolean[n][n];
		Queue<int[]> q = new LinkedList<>();
		int[][] dirs = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
		visit[x][y] = true;
		q.add(new int[]{x, y});
		while( !q.isEmpty() ){
			int[] pair = q.poll();
			for(int[] dir : dirs){
				int i = dir[0] + pair[0];
				int j = dir[1] + pair[1];
				if( i == n-1 && j == n-1 && maze[i][j] == '@' ){
					System.out.println("path Exist");
					System.exit(0);
				}
				if( i >=0 && j >= 0 && i < n && j < n && !visit[i][j] && maze[i][j] == '.' ){
					try{
						clearScreen();
						Thread.sleep(0);
					}catch(Exception ee){
						System.out.println(ee);
					}
					q.add(new int[]{i, j});
					visit[i][j] = true;
					maze[i][j] = (char)1;
					print(maze);
					maze[i][j] = '.';
				}
			}
		}
	}
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		int n = sn.nextInt();
		char[][] mazeboard = new char[n][n];
		String s = (char)127+"..";
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				mazeboard[i][j] = s.charAt(rn.nextInt(3));
			}
		}
		mazeboard[0][0] = '.';
		mazeboard[n-1][n-1] = '@';
		new Maze().print(mazeboard);
		//int m = sn.nextInt();
		boolean[][] visit = new boolean[n][n];
		new Maze().dfs(mazeboard, 0, 0, mazeboard.length, visit, (char)26);
		// new Maze().bfs(mazeboard, 0, 0);
		System.out.println("Path not Exist");
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
