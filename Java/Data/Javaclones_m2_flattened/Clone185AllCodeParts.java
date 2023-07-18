public class Clone185AllCodePartsm2 {  
 public void run () { 
     try { 
         Thread t = new Thread (new Lock ()); 
         t.start (); 
         t.join (); 
     } catch (InterruptedException ex) { 
         System.out.println ("won't see me"); 
     } 
 }

public void run () {
System.out.println("Thread " + Thread.currentThread().getId() + " starting");
System.out.println("Thread " + Thread.currentThread().getId() + " acquired the monitor on BadRunnable.class");
latch.countDown();
while(true)
latch.await();
System.out.println("Thread " + Thread.currentThread().getId() + " released the monitor on BadRunnable.class");
System.out.println("Thread " + Thread.currentThread().getId() + " ending");
}

}