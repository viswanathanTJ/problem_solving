import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        String s = "Vviswa";
        System.out.println((int)'z');
        for(char c: s.toCharArray()) {
            char in = c>96 ? 'a' : 'A';
            System.out.println(c-in);
        }
    }
}