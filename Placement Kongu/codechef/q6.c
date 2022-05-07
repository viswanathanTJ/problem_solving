/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
    static boolean checkSorted(int n, String arr) {
        char[] b = new char[n];

        for(int i=0;i<n;i++)
            b[i] = arr.charAt(i);
        Arrays.sort(b, 0, n);
        int ct = 0;
        for (int i = 0; i < n; i++)
            if (arr.charAt(i) != b[i])
                ct++;
        if (ct == 0 || ct == 2)
            return true;
        else
            return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t,n;
        String s;
        t = sc.nextInt();
        while(t-->0) {
            n = sc.nextInt();
            s = sc.next();
            if (checkSorted(n, s))
                System.out.println("YES");
            else
               System.out.println("NO");
        }
    }
}