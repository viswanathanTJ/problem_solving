import java.io.*;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws Exception {
        code object = new code();
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        String[] str1 = buf.readLine().split(" ");
        int P = Integer.parseInt(str1[0]);
        int Q = Integer.parseInt(str1[1]);
        int N = Integer.parseInt(str1[2]);

        int[] aliens = new int[N];
        int[] golds = new int[N];
        for (int i = 0; i < N; i++) {
            String[] temp = buf.readLine().split(" ");
            aliens[i] = Integer.parseInt(temp[0]);
            golds[i] = Integer.parseInt(temp[1]);
        }

        object.Gold(P, Q, N, aliens, golds);
    }
}

class code {
    void Gold(int P, int Q, int n, int[] alien, int[] gold) {
        if (n == 2) {
            if ((alien[0] < P && alien[1] < P && alien[0] < Q && alien[1] < Q)
                    || (alien[0] > P && alien[1] < 2 * P && alien[0] < Q && alien[1] < Q)) {
                System.out.println(Math.max(gold[0], gold[1]));
            } else {
                System.out.println(0);
            }
        } else {
            int val = P / Q;
            if (val % 2 != 0 || val == 0) {
                Arrays.sort(gold);
                int s = 0;
                for (int i = 0; i < n; i++)
                    s += gold[i];
                System.out.println(s - gold[0]);
            } else {
                int s = 0;
                for (int i = 0; i < n; i++)
                    s += gold[i];
                System.out.println(s);
            }
        }
    }
}