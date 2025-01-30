import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Solution {

    public static int kadane(int nums[]) throws Exception {
        int max = nums[0], sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (sum < 0) sum = 0;
            sum = sum + nums[i];
            if (sum > max) max = sum;
        }
        return max;
    }

    public static void main(String args[]) throws Exception {
        Scanner sn = new Scanner(System.in);
        int testCase = sn.nextInt();
        sn.nextLine(); // consume leftover newline
        // System.out.println(factorial(6));
        int[] inp = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        // kadane(inp);
        int[] inp1 = new int[]{-2, 1};
        System.out.println(kadane(inp1));


        sn.close();
    }
}