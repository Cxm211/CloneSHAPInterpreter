public class Clone687AllCodeParts { 
synchronized public void print () throws InterruptedException {
while(count < 15)
for([int i=0] i < 5 [i++])
count++;
System.out.println(count + " -- " + Thread.currentThread());
notifyAll();
wait();
}
 
 public void print () { 
     try { 
         waitForSemaphore.acquire (); 
         int start = nextStartIdx; 
         for (int i = 0; 
         i < 5; i ++) { 
             System.out.println (String.format ("%d -- %s", i + start, Thread.currentThread ().getName ())); 
         } 
         nextStartIdx += 5; 
         next.release (); 
     } catch (InterruptedException ie) { 
         Thread.currentThread ().interrupt (); 
     } 
 }

}