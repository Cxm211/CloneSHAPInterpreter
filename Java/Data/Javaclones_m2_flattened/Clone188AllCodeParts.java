public class Clone188AllCodePartsm2 {  
 public void run () { 
     System.out.println ("Thread " + Thread.currentThread ().getId () + " starting"); 
     synchronized (BadRunnable.class) { 
         System.out.println ("Thread " + Thread.currentThread ().getId () + " acquired the monitor on BadRunnable.class"); 
         latch.countDown (); 
         while (true) { 
             try { 
                 latch.await (); 
             } catch (InterruptedException ex) { 
                 continue; 
             } 
             break; 
         } 
     } 
     System.out.println ("Thread " + Thread.currentThread ().getId () + " released the monitor on BadRunnable.class"); 
     System.out.println ("Thread " + Thread.currentThread ().getId () + " ending"); 
 }

public void run () {
String threadName=Thread.currentThread().getName();
first.lock();
latch.countDown();
System.out.println(threadName + ": locked first lock");
latch.await();
System.out.println(threadName + ": attempting to lock second lock");
second.lock();
System.out.println(threadName + ": never reached");
}

}