public class Clone184AllCodeParts { 
public void run () {
System.out.println("Outer launched");
System.out.println("Obtaining lock");
Thread inner=new Thread(new InnerTask(lock),"inner");
inner.start();
inner.join();
e.printStackTrace();
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