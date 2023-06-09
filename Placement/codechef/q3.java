/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class q3 {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        Interval[] ni = new Interval[n];
        Interval[] mi = new Interval[m];

        for (int i = 0; i < n; i++) {
            long start = sc.nextLong();
            long end = sc.nextLong();
            ni[i] = new Interval(start, end);
        }

        for (int i = 0; i < m; i++) {
            long start = sc.nextLong();
            long end = sc.nextLong();
            mi[i] = new Interval(start, end);
        }
        Arrays.sort(ni, Comparator.comparingLong(b -> b.start));
        Arrays.sort(mi, Comparator.comparingLong(b -> b.start));
        long ans = 0;
        int i = 0, j = 0;
        while (i < n && j < m) {
            long l = max(ni[i].start, mi[j].start);
            long r = min(ni[i].end, mi[j].end);

            if (l <= r)
                ans += r - l;

            if (ni[i].end < mi[j].end)
                i++;
            else
                j++;
        }
        System.out.println(ans);
    }

    static long max(long a, long b) {
        return a > b ? a : b;
    }

    static long min(long a, long b) {
        return a < b ? a : b;
    }

    static class Interval {
        long start;
        long end;

        Interval(long s, long e) {
            start = s;
            end = e;
        }
    }
}