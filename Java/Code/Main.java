import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class Main {
    static void getReverseStrings(List<String> arr) {
        
    }
    public static void main(String[] args) {
        var stringList = new ArrayList<String>(){
            {
                add("abc");
                add("cba");
            }
        };
        var strings = new ArrayList<>(Arrays.asList("abc","cba"));
        System.out.println(stringList);
        System.out.println(strings);
    }
}