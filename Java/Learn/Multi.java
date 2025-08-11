class MyThread extends Thread {
    public void run() {
        System.out.println("MyThread");
    }
}

class MyRun implements Runnable {
    public void run() {
        System.out.println("MyRun");
    }
}

class Multi {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();   
        Thread thread = new Thread(new MyRun());
        thread.start();
    }
}