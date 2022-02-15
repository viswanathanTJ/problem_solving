import java.io.*;
import java.util.*;
class NQueensRowWise{
	static boolean isSafe(int n, char[][] board, int r, int c){
		for( int i=0;i<r;i++ ){
			if( board[i][c] == 'Q' )
				return false;
		}
		for( int i=r, j=c; i>=0 && j>=0; i--, j-- ){
			if( board[i][j] == 'Q' )
				return false;
		}
		for( int i=r, j=c; i>=0 && j<n; i--, j++ ){
			if( board[i][j] == 'Q' )
				return false;
		}
		return true;
	}
	static boolean solve(int n, char[][] board, int r){
		if( r >= n )
			return true;
		for( int i=0;i<n;i++ ){
			if( isSafe(n, board, r, i) ){
				board[r][i] = 'Q';
				if( solve(n, board, r+1) )
					return true;
				board[r][i] = '.';
			}
		}
		return false;
	}
	static final Scanner sn = new Scanner(System.in);
	static final Random rn = new Random();
	public static void main(String[] args) {
		int n = sn.nextInt();
		char[][] board = new char[n][n];
		for( int i=0;i<n;i++ )
			Arrays.fill(board[i], '.');
		solve(n, board, 0);
		System.out.println("SOLUTION : ");
		for(char[] ar : board){
			for(char ch : ar){
				System.out.print(ch+" ");
			}
			System.out.println();
		}
	}
}