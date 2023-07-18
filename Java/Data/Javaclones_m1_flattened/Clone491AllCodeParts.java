public class Clone491AllCodeParts { 
public void run () {
while(true)
while(current.equals(info))
signal.wait();
System.out.println(info);
current=info;
signal.notify();
}
 
 public synchronized void run () { 
     try { 
         while (true) { 
             System.out.println (info); 
             wait (); 
         } 
     } catch (Exception e) { 
     } 
 }

}