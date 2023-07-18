public class Clone188AllCodeParts { 
public void run () {
System.out.println("Thread " + Thread.currentThread().getId() + " starting");
System.out.println("Thread " + Thread.currentThread().getId() + " acquired the monitor on BadRunnable.class");
latch.countDown();
while(true)
latch.await();
System.out.println("Thread " + Thread.currentThread().getId() + " released the monitor on BadRunnable.class");
System.out.println("Thread " + Thread.currentThread().getId() + " ending");
}
 
 public void run () { 
     String threadName = Thread.currentThread ().getName (); 
     try { 
         first.lock (); 
         latch.countDown (); 
         System.out.println (threadName + ": locked first lock"); 
         latch.await (); 
         System.out.println (threadName + ": attempting to lock second lock"); 
         second.lock (); 
         System.out.println (threadName + ": never reached"); 
     } catch (InterruptedException e) { 
         throw new RuntimeException (e); 
     } 
 }

}