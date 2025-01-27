import java.util.Scanner;

public class Solution {
    public static void printMatrix(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        for (int i=0; i<n; i++) { 
            for (int j=0; j<m; j++)  {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void setZeroes(int[][] matrix) {
        int row0 = 1;
        int n = matrix.length;
        int m = matrix[0].length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    if (i == 0) {
                        row0 = 0;
                    } else {
                        matrix[i][0] = 0;
                    }
                }
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (matrix[i][j] != 0) {
                    if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                        matrix[i][j] = 0;
                    }
                }
            }
        }

        if (matrix[0][0] == 0) {
            for (int i = 0; i < n; i++) {
                matrix[i][0] = 0;
            }
        }

        if (row0 == 0) {
            for (int j = 0; j < m; j++) {
                matrix[0][j] = 0;
            }
        }
    }

    public static void main(String args[]) throws Exception {
        Scanner sn = new Scanner(System.in);
        int testCase = sn.nextInt();
        sn.nextLine(); // consume leftover newline
        
        for(int i=0; i<testCase; i++){
            String input = sn.nextLine();
            // Remove outer square brackets and split by "],[" pattern
            input = input.substring(2, input.length()-2); // remove "[[" and "]]"
            String[] inputArray = input.split("],\\[");
            int[][] matrix = new int[inputArray.length][inputArray[0].split(",").length];
            for(int j=0; j<inputArray.length; j++){
                String[] row = inputArray[j].split(",");
                for(int k=0; k<row.length; k++){
                    matrix[j][k] = Integer.parseInt(row[k]);
                }
            }
            setZeroes(matrix);
            printMatrix(matrix);
            System.out.println("done");
        }

        sn.close();
    }
}