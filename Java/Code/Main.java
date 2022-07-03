interface A{
    int x=65;
}
interface B{
    int x=66;
}
public class Main implements A,B {
    public static void main(String[] a){
        System.out.println(B.x); // which x?
    }
}