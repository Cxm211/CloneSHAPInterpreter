public class Clone491AllCodePartsm2 {  
 public void run () { 
     try { 
         synchronized (signal) { 
             while (true) { 
                 while (current.equals (info)) signal.wait (); 
                 System.out.println (info); 
                 current = info; 
                 signal.notify (); 
             } 
         } 
     } catch (Exception e) { 
     } 
 }

public synchronized void run () {
while(true)
System.out.println(info);
wait();
}

}