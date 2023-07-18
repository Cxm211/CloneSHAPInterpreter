public class Clone313AllCodePartsm2 {  
 public void run () { 
     try { 
         for (Map.Entry < Integer, Integer > entry : map.entrySet ()) { 
             if (entry.getKey ().equals (Integer.valueOf (10))) { 
                 try { 
                     writeLatch.countDown (); 
                     readLatch.await (); 
                 } catch (InterruptedException e) { 
                     Thread.currentThread ().interrupt (); 
                 } 
             } 
         } 
     } catch (Exception e) { 
         e.printStackTrace (); 
     } 
 }

public void run () {
for([int i=0] null [i++])
if(i % 1000 == 0)
System.out.printf("get: %d\n",i);
Map<K,String> m2=new HashMap<>(map);
}

}