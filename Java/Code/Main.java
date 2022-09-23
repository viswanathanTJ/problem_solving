class Main {
    static void getPermutations(int[] arr) {
        helper(arr, 0);
    }

    static void helper(int[] arr, int pos) {
        if(pos > arr.length-1) {
            for(int i=0;i<pos;i++) {
                System.out.print(arr[i]+",");
            }
            System.out.println();
        }
        for(int i=pos;i<arr.length;i++) {
            int t = arr[pos];
            arr[pos] = arr[i];
            arr[i] = t;

            helper(arr, pos+1);

            t = arr[pos];
            arr[pos] = arr[i];
            arr[i] = t;
        }
        
    }



    public static void main(String[] args) {
        getPermutations(new int[] {1,2,3,4});
    }
}