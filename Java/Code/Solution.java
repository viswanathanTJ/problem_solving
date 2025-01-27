import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Solution {
    public static List<List<Integer>> generate(int numRows) {
        if (numRows == 0) {
            return new ArrayList<>();
        }
        List<List<Integer>> result = new ArrayList<>(Arrays.asList(Arrays.asList(1)));
        for (int i = 1; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            List<Integer> prevRow = result.get(i-1);
            row.add(1);
            for (int j = 1; j < i; j++) 
                row.add(prevRow.get(j-1)+prevRow.get(j));
            row.add(1);

            result.add(row);
        }
        return result;
    }

    public static void main(String args[]) throws Exception {
        Scanner sn = new Scanner(System.in);
        int testCase = sn.nextInt();
        sn.nextLine(); // consume leftover newline
        System.out.println(generate(testCase));
        sn.close();
    }
}