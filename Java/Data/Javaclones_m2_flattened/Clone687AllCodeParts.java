public class Clone687AllCodePartsm2 {  
 synchronized public void print () throws InterruptedException { 
     while (count < 15) { 
         for (int i = 0; 
         i < 5; i ++) { 
             count ++; 
             System.out.println (count + " -- " + Thread.currentThread ()); 
         } 
         notifyAll (); 
         wait (); 
     } 
 }

public void print () {
waitForSemaphore.acquire();
int start=nextStartIdx;
for([int i=0] i < 5 [i++])
System.out.println(String.format("%d -- %s",i + start,Thread.currentThread().getName()));
nextStartIdx+=5;
next.release();
Thread.currentThread().interrupt();
}

}