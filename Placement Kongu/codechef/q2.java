/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class q2 {
    public static void main(String[] args) throws java.lang.Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine());
        if (size <= 0) {
            System.out.println("Invalid Input");
            return;
        }
        List<String> arr = new ArrayList<>();
        while (size-- > 0) {
            String[] str = br.readLine().split(" ");
            String pattern1 = "[a-m]+";
            String pattern2 = "[N-Z]+";
            int words = Integer.parseInt(str[0]);
            boolean flag = true;
            for (int i = 1; i <= words; i++) {
                boolean match1 = str[i].matches(pattern1);
                boolean match2 = str[i].matches(pattern2);
                if ((match1 && match2) || (!match1 && !match2)) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                arr.add("YES");
            else
                arr.add("NO");

        }
        for (String s : arr)
            System.out.println(s);
    }
}
