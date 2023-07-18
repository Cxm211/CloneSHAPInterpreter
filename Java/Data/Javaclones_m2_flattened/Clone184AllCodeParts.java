public class Clone184AllCodePartsm2 {  
 public void run () { 
     System.out.println ("Outer launched"); 
     System.out.println ("Obtaining lock"); 
     synchronized (lock) { 
         Thread inner = new Thread (new InnerTask (lock), "inner"); 
         inner.start (); 
         try { 
             inner.join (); 
         } catch (InterruptedException e) { 
             e.printStackTrace (); 
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