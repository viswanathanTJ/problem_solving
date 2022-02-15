import java.util.*;
import java.io.*;


class Main {
   
    public static void main(String[] args) {
        int arr[] = new int[] { 1,2,2,1,2 };
        int n = 5;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = i+2; j < n; j++) {
                if (i != j) {
                    map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
                }
            }
        }
        System.out.println(map);
    }
}