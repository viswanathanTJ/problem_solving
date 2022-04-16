class Main{
    static long sol[] = new long[1000001];
    
    static class Trie{
        int count;
        Trie link[];
        
        public Trie(){
            count = 0;
            link = new Trie[26];
        }
    }
    
    static Trie root = new Trie();
    
    public static void addString(String s){
        int l = s.length();
        Trie ptr = root;
        
        for(int i=0; i<l; i++){
            int curr = s.charAt(i)-'a';
            
            if(ptr.link[curr] == null){
                sol[i] = sol[i] + (long)ptr.count;
                ptr.link[curr] = new Trie();
            }
            else{
                sol[i] = sol[i]+(long)(ptr.count-ptr.link[curr].count);
                if(i == l-1)
                    sol[i+1] = sol[i+1] + ptr.link[curr].count;
            }
            ptr.count++;
            ptr = ptr.link[curr];
        }
        ptr.count++;
    }
    public static void main(String args[] ) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ml = 0;
        while(n-- > 0){
            String s = br.readLine();
            if(s.length() > ml)
                ml = s.length();
            addString(s);
        }
        
        for(int i=0; i<=ml; i++)
            System.out.print(sol[i]+" "); 
    }
}