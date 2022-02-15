import java.io.*;
import java.util.*;
class NQueen{
	//just test
	public static boolean isSafe(int[][] board, int row, int col, int n){
		//row
		for( int i=col; i>=0; i-- )
			if( board[row][i] == 1 )
				return false;
		//upper diagonal
		for( int i=row, j=col; i>=0 && j>=0; i--, j-- )
			if( board[i][j] == 1 )
				return false;
		//lower diagnol
		for( int i=row, j=col; i<n && j>=0; i++, j-- )
			if( board[i][j] == 1 )
				return false;
		return true;
	}
	public static boolean solve(int[][] board, int col, int n){
		if( col == n )
			return true;
		for(int i=0; i<n; i++){
			if( isSafe(board, i, col, n) ){
				board[i][col] = 1;
				if( solve(board, col+1, n) )
					return true;
				board[i][col] = 0;
			}
		}
		return false;
	}
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		int n = sn.nextInt();
		int[][] board = new int[n][n];
		for(int i=0; i<n; i++)
			Arrays.fill(board[i], 0);
		if( solve(board, 0, n) == true ){
			System.out.println("solved");
			print(board);
		}
	}
	public static void print(int[][] board){
		for(int[] ar : board){
			for(int x : ar)
				System.out.print(x+" ");
			System.out.println();
		}
	}
}
