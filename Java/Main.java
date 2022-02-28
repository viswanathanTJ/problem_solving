import java.io.*;
import java.util.*;

class Main {
    public static int dfs(int[][] mat) {
        int r = mat.length;
        int c = mat[0].length;
        boolean[][] visit = new boolean[r][c];
        for (int i = 0; i < r; i++)
            Arrays.fill(visit[i], false);
        int count = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (!visit[i][j] && mat[i][j] == 1) {
                    dfs(i, j, mat, visit);
                    count++;
                }
            }
        }
        return count;
    }

    public static void dfs(int i, int j, int[][] mat, boolean[][] visit) {
        if (i < 0 || j < 0 || i >= mat.length || j >= mat[0].length || visit[i][j] || mat[i][j] == 0)
            return;
        visit[i][j] = true;
        dfs(i + 1, j, mat, visit);
        dfs(i - 1, j, mat, visit);
        dfs(i, j + 1, mat, visit);
        dfs(i, j - 1, mat, visit);

        dfs(i + 1, j + 1, mat, visit);
        dfs(i - 1, j - 1, mat, visit);
        dfs(i + 1, j - 1, mat, visit);
        dfs(i - 1, j + 1, mat, visit);
    }


    
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        int r = sn.nextInt();
        int c = sn.nextInt();
        int[][] mat = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                mat[i][j] = sn.nextInt();
            }
        }
        System.out.println(dfs(mat));
    }
}
