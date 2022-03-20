import java.util.*;

class Soln {
    public int closestPair(int input1, int[] input2) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < input1; i++)
            for (int j = 0; j < input1; j++)
                if(i!=j)
                    if(input2[i] > input2[j])
                        res = Math.min(input2[i] - input2[j], res);
        return res;
    }

    public int sum(int input1, int[] input2) {
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        for (int i = 0; i < input1; i++) {
            if (input2[i] < min)
                min = input2[i];
            if (input2[i] > max)
                max = input2[i];
        }
        return max + min;
    }
    
    public int lastdigit(int input1, int input2) {
        int p = (int) Math.pow(input1, input2);
        return p % 10;
    }
    
    public int countDecoding(String input1) {
        char[] arr = input1.toCharArray();
        return countDecodingSolve(arr, arr.length);
    }
    public static int countDecodingSolve(char[] digits, int n) {
        if (n == 0 || n == 1)
            return 1;

        if (digits[0] == '0')
            return 0;
        int count = 0;
        if (digits[n - 1] > '0')
            count = countDecodingSolve(digits, n - 1);
        if (digits[n - 2] == '1'
                || (digits[n - 2] == '2'
                        && digits[n - 1] < '7'))
            count += countDecodingSolve(digits, n - 2);

        return count;
    }
    

    public static String factorial(int input1) {
        int f = 1;
        for (int i = 1; i <= input1; i++)
            f *= i;
        return f+"";
    }

    static int arrangements(int input1) {
        if (input1 == 1)
            return 0;
        if (input1 == 2)
            return 1;

        return (input1 - 1) * (arrangements(input1 - 1) +
                arrangements(input1 - 2));
    }

    public static int evalInfix(String expression) {
        char[] tokens = expression.toCharArray();

        Stack<Integer> values = new Stack<Integer>();

        Stack<Character> ops = new Stack<Character>();

        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i] == ' ')
                continue;
            if (tokens[i] >= '0' &&
                    tokens[i] <= '9') {
                StringBuffer sbuf = new StringBuffer();
                while (i < tokens.length &&
                        tokens[i] >= '0' &&
                        tokens[i] <= '9')
                    sbuf.append(tokens[i++]);
                values.push(Integer.parseInt(sbuf.toString()));
                i--;
            }
            else if (tokens[i] == '(')
                ops.push(tokens[i]);
            else if (tokens[i] == ')') {
                while (ops.peek() != '(')
                    values.push(applyOp(ops.pop(),
                            values.pop(),
                            values.pop()));
                ops.pop();
            }
            else if (tokens[i] == '+' ||
                    tokens[i] == '-' ||
                    tokens[i] == '*' ||
                    tokens[i] == '/') {
                while (!ops.empty() &&
                        hasPrecedence(tokens[i],
                                ops.peek()))
                    values.push(applyOp(ops.pop(),
                            values.pop(),
                            values.pop()));

                ops.push(tokens[i]);
            }
        }

        while (!ops.empty())
            values.push(applyOp(ops.pop(),
                    values.pop(),
                    values.pop()));

        return values.pop();
    }

    public static boolean hasPrecedence(
            char op1, char op2) {
        if (op2 == '(' || op2 == ')')
            return false;
        if ((op1 == '*' || op1 == '/') &&
                (op2 == '+' || op2 == '-'))
            return false;
        else
            return true;
    }

    public static int applyOp(char op,
            int b, int a) {
        switch (op) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                if (b == 0)
                    throw new UnsupportedOperationException(
                            "Cannot divide by zero");
                return a / b;
        }
        return 0;
    }

    public static String reverseString(String input1) {
        String[] arrOfStr = input1.split(" ");
        StringBuilder res = new StringBuilder();
        for (int i = arrOfStr.length - 1; i >= 0; i--)
            res.append(arrOfStr[i]+" ");
        return res.toString();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println(factorial(5));
        System.out.println(reverseString("hello world"));
        // int n = sc.nextInt();
        // int[] arr = new int[n];
        // for (int i = 0; i < n; i++)
        //     arr[i] = sc.nextInt();
        // sc.close();
        // Soln obj = new Soln();
        // System.out.println(obj.closestPair(n, arr));
    }
}