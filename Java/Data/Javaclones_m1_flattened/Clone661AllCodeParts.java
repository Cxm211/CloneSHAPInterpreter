public class Clone661AllCodeParts { 
public void run () {
int i=1;
while(true)
System.out.println(i);
Thread.sleep(1000);
cb.await();
e.printStackTrace();
e.printStackTrace();
i=i + 3;
}
 
 public void run () { 
     System.out.println (i); 
     try { 
         cb.await (); 
         i = i + 3; 
         Thread.sleep (1000); 
     } catch (InterruptedException e) { 
         e.printStackTrace (); 
     } catch (BrokenBarrierException e) { 
         e.printStackTrace (); 
     } 
 }

}