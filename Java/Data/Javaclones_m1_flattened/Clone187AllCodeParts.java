public class Clone187AllCodeParts { 
public void run () {
latch.countDown();
latch.await();
System.out.println("Thread finished");
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