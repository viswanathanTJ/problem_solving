import java.util.*;


class Soln {
    public int countLuck(String s) {
        char[] a = s.toCharArray();
        int luck = 0;
        int count = 0;
        for (int i = 0; i < a.length; ++i) {
            if (a[i] == ' ') {
                if (count >= 4)
                    ++luck;
                count = 0;
            } else if (((int) (a[i] - 'a')) % 2 == 0)
                ++count;
        }
        return luck;
    }

    public void luckiest(String[] a) {
        int[] c = new int[a.length];
        int max1 = -1;
        for (int i = 0; i < a.length; ++i) {
            c[i] = countLuck(a[i]);
            if (max1 < 0)
                max1 = i;
            else if (c[i] > c[max1])
                max1 = i;
        }
        System.out.println(a[max1]);
        int max2 = -1;
        for (int i = 0; i < a.length; ++i) {
            if (i == max1)
                continue;
            if (max2 < 0)
                max2 = i;
            else if (c[i] > c[max2])
                max2 = i;
        }
        System.out.println(a[max2]);
    }

    public static void main(String[] args) {
        Soln obj = new Soln();
        String[] arr = { "KRKRKKR" };
        obj.luckiest(arr);
    }
}