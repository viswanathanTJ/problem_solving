import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

class Main {
    
   public static void main (String[] args)
    {
        Student s = new Student("viswa", 22);
        String fileName = "test.txt";
        FileOutputStream fileOut = null;
        ObjectOutputStream objOut = null;
        
        try {
            fileOut = new FileOutputStream(fileName);
            objOut = new ObjectOutputStream(fileOut);

            objOut.writeObject(s);
            objOut.close();
            fileOut.close();
            System.out.println("Object has been serialized to file");
        } catch(IOException ex) {
            System.out.println("IOException occurred");
            ex.printStackTrace();
        }

        System.out.println(s);
    }
}