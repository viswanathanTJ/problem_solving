import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    public static void sortColors(int[] nums) {
        int n = nums.length;
        int l = 0, m = 0, r = n - 1;
        while (m <= r) {
            int t = nums[m];
            if (t == 0) {
                nums[m] = nums[l];
                nums[l] = t;
                l++; m++;
            } else if (nums[m] == 2) {
                nums[m] = nums[r];
                nums[r] = t;
                r--;
            } else {
                m++;
            }
        }
    }

    public static void main(String args[]) throws Exception {
        Scanner sn = new Scanner(System.in);
        int testCase = sn.nextInt();
        sn.nextLine(); // consume leftover newline
        for (int i = 0; i < testCase; i++) {
            String s = sn.nextLine();
            String[] arr = s.substring(1, s.length() - 1).split(",");
            int[] nums = Arrays.stream(arr).mapToInt(Integer::parseInt).toArray();
            sortColors(nums);
            System.out.println(Arrays.toString(nums));
        }
        sn.close();
    }
}