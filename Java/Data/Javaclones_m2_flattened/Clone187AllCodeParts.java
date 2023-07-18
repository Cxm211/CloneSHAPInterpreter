public class Clone187AllCodePartsm2 {  
 public void run () { 
     synchronized (obj1) { 
         latch.countDown (); 
         try { 
             latch.await (); 
         } catch (InterruptedException e) { 
             throw new RuntimeException (); 
         } 
         synchronized (obj2) { 
             System.out.println ("Thread finished"); 
         } 
     } 
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