import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    public static int maxProfit(int[] prices) {
        int n = prices.length;
        int profit = Integer.MIN_VALUE;
        int lowest_price = prices[0];
        for (int i = 0; i < n; i++) {
            if (prices[i] < lowest_price) lowest_price = prices[i];
            else  profit = Math.max(prices[i] - lowest_price, profit);
        }

        return profit >= 0 ? profit : 0;
    }

    public static void main(String args[]) throws Exception {
        Scanner sn = new Scanner(System.in);
        int testCase = sn.nextInt();
        sn.nextLine(); // consume leftover newline
        for (int i = 0; i < testCase; i++) {
            String s = sn.nextLine();
            String[] arr = s.substring(1, s.length() - 1).split(",");
            int[] nums = Arrays.stream(arr).mapToInt(Integer::parseInt).toArray();
            int res = maxProfit(nums);
            System.out.println(res);
        }
        sn.close();
    }
}