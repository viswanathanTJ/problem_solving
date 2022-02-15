import java.io.*;
import java.util.*;
class NQueensColumnWise{
	// public static int n;
	public static boolean isSafe(int n, char[][] board, int r, int c){
		for( int i=0;i<c;i++ ){
			if( board[r][i] == 'Q' )
				return false;
		}
		for( int i=r, j=c; i>=0 && j>=0; i--, j-- ){
			if( board[i][j] == 'Q' )
				return false;
		}
		for( int i=r, j=c; i<n && j>=0; i++, j-- ){
			if( board[i][j] == 'Q' )
				return false;
		}
		return true;
	}
	public static boolean solve(int n, char[][] board, int col){
		try{
			// Runtime.getRuntime().exec("cls");
			/*System.out.print("\033[H\033[2J");
			System.out.flush();*/
			new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
			Thread.sleep(0);
			print(board);
			if( col >= n )
				return true;
			for(int i=0;i<n;i++){
				if( isSafe(n, board, i, col) ){
					// System.out.print(isSafe(board, i, col)+" ");
					board[i][col] = 'Q';
					if(solve(n, board, col+1))
						return true;
					board[i][col] = '.';
				}
			}
		}catch(Exception e){
			System.out.println(e+"");
		}
		return false;
	}
	public static void print(char[][] board){
		for(char[] ar : board){
			for(char ch : ar)
				System.out.print(ch+" ");
			System.out.println();
		}
	}
	public static final Scanner sn = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.println("enter board size : ");
		int n = sn.nextInt();
		char[][] board = new char[n][n];
		for(int i=0;i<n;i++){
			Arrays.fill(board[i], '.');
		}
		System.out.println("Generated Board : ");
		print(board);
		solve(n, board, 0);
		/*System.out.println("SOLVED");
		print(board);*/
	}
}