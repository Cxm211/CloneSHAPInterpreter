public class Clone661AllCodePartsm2 {  
 public void run () { 
     int i = 1; 
     while (true) { 
         System.out.println (i); 
         try { 
             Thread.sleep (1000); 
             cb.await (); 
         } catch (InterruptedException e) { 
             e.printStackTrace (); 
         } catch (BrokenBarrierException e) { 
             e.printStackTrace (); 
         } 
         i = i + 3; 
     } 
 }

public void run () {
System.out.println(i);
cb.await();
i=i + 3;
Thread.sleep(1000);
e.printStackTrace();
e.printStackTrace();
}

}