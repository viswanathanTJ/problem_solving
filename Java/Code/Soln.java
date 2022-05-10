import java.util.Scanner;

class Soln {
    public static final Scanner s = new Scanner(System.in);
    
    public static void main(String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);
        int i, j, n, t, a, r, c, max, min;
        t = sc.nextInt();
        int res = Integer.MIN_VALUE;
        while (t-- > 0) {
            r = sc.nextInt();
            c = sc.nextInt();
            for (i = 0; i < r; i++) {
                max = Integer.MIN_VALUE;
                min = Integer.MAX_VALUE;
                for (j = 0; j < c; j++) {
                    a = sc.nextInt();
                    if (a > max)
                        max = a;
                    if (a < min)
                        min = a;
                }
                res = Math.max(max - min, res);
            }
            System.out.println(res);
        }
    }
}