import java.io.*;
import java.util.*;
class Main{
    static class Node{
        Node left, right;
        int val;
        Node(int val){
            this.val = val;
            left = right = null;
        }
    }
    public static Node insert(Node root, int val){
        if(root==null) return new Node(val);
        if(root.val<val) root.right = insert(root.right, val);
        if(root.val>val) root.left = insert(root.left, val);
        return root;
    }
    public static void print(Node root){
        Map<Integer, List<Integer>> map = new TreeMap<>();
        dfs(map, root, 0);
        for(Map.Entry<Integer, List<Integer>> m : map.entrySet()){
            m.getValue().forEach((x)->System.out.print(x+" "));
            System.out.println();
        }
    }
    public static void dfs(Map<Integer, List<Integer>> map, Node root, int ind){
        if(root==null) return;
        if(!map.containsKey(ind)) map.put(ind, new ArrayList<>());
        map.get(ind).add(root.val);
        if(root.left!=null) dfs(map, root.left, ind-1);
        if(root.right!=null) dfs(map, root.right, ind+1);
    }
    public static final Scanner sn = new Scanner(System.in);
    public static void main(String[] asdf){
        Node root = null;
        while(true){
            int n = sn.nextInt();
            if(n<1) break;
            root = insert(root, n);
        }
        print(root);
    }
}