public class Clone459AllCodeParts { 
public void run () {
while(true)
String output=task();
if(output != null)
int count=counter.getAndIncrement();
System.out.println(output);
if(count >= 100)
}
 
 public void run () { 
     while (true) { 
         try { 
             Object expensiveObject = expensiveObjects.take (); 
             String output = task (); 
             expensiveObjects.put (expensiveObject); 
             if (output != null) { 
                 int counter = outputCount.getAndIncrement (); 
                 System.out.println (counter); 
                 if (counter >= 100) { 
                     break; 
                 } 
             } 
         } catch (InterruptedException e) { 
             System.out.println ("Error!"); 
         } 
     } 
 }

}