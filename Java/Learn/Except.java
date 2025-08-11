class MyException extends Exception {
    @Override
    public String toString() {
        return "MyException";
    }
}

public class Except {
    public static void main(String[] args) throws MyException {
        try {
            if(1 < 2) {
                throw new MyException();
            }
        } catch (MyException e) {
            System.out.println("Caught MyException");
            System.out.println(e);
        }
    }
}
