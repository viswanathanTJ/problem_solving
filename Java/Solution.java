import java.util.*;

class Solution 
{
    public static boolean check(int[] a, int[] b) {
        for(int i=0;i<26;i++)
            if(a[i] != b[i]) return false;
        return true;
    }
    public static boolean checkString(String s1, String s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 > n2)
            return false;
        int[] a = new int[26];
        int[] b = new int[26];
        int i;
        for (i = 0; i < n1; i++)
            a[s1.charAt(i) - 'a']++;
        for (i = 0; i < n1; i++)
            b[s2.charAt(i) - 'a']++;
        if (check(a, b))
            return true;
        for (i = n1; i < n2; i++) {
            b[s2.charAt(i) - 'a']++;
            b[s2.charAt(i - n1) - 'a']--;
            if (check(a, b))
                return true;
        }
        return false;

    }
    public static void main(String arg[]) 
    {
        Scanner sc = new Scanner(System.in);
        String s1 = "abcdef";
        String s2 = "abcdfg";
        System.out.println((int)s1.charAt(4));
    } 
}