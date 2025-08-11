import java.io.*;

class Buffered {
    public static void main(String[] args) {
        // StringBuilder sb = new StringBuilder();
        // try {
        //     FileInputStream fin = new FileInputStream("D:\\WorkSpace\\problem_solving\\input.txt");
        //     BufferedInputStream bin = new BufferedInputStream(fin);
            // int i;
            // while ((i = bin.read()) != -1) {
            //     sb.append((char) i);
            //     System.out.print((char) i);
            // }
        //     bin.close();
        //     fin.close();
        // } catch (Exception e) {
        //     System.out.println(e);
        // }
        // System.out.println(sb.toString());
        try {
            FileOutputStream fout = new FileOutputStream("D:\\WorkSpace\\problem_solving\\output.txt");
            BufferedOutputStream bout = new BufferedOutputStream(fout);
            // bout.write(sb.toString().getBytes());
            String s = "My content";
            byte[] b = s.getBytes();
            bout.write(s.getBytes());
            bout.write(s.getBytes());
            bout.flush();
            bout.close();
            fout.close();
            System.out.println("success");
        } catch (Exception e) {
            System.out.println(e);
        }


    }
}