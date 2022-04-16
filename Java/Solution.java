import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String args[]) throws Exception {

        Scanner sn = new Scanner(System.in);
        int n = sn.nextInt();
        Stack<Integer> s = new Stack<Integer>();
        while (n-- > 0) {
            int q = sn.nextInt();
            if (q == 1)
                s.push(sn.nextInt());
            else if (q == 2) {
                int k = sn.nextInt();
                int ind = sn.nextInt();
                List<Integer> list = new ArrayList<Integer>();
                for (int i = 0; i < s.size(); i++)
                    list.add(s.get(i) ^ k);
                Collections.sort(list);
                System.out.println(list.get(ind-1));
            }
        }
    }
}