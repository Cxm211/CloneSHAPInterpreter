public class Clone457AllCodeParts { 
public static void main (String [] args) throws InterruptedException { 
     CountDownLatch theLatch = new CountDownLatch (100); 
     List < String > output = Collections.synchronizedList (new ArrayList < String > ()); 
     SecureRandom random = new SecureRandom (); 
     ExecutorService service = Executors.newCachedThreadPool (); 
     for (int i = 0; 
     i < 4; i ++) { 
         service.execute (new CountDownTask (theLatch, output, random)); 
     } 
     theLatch.await (1, TimeUnit.MINUTES); 
     service.shutdown (); 
     System.out.println (output.size ()); 
 } 
 
public static void main (String [] args) throws InterruptedException {
AtomicInteger counter=new AtomicInteger();
ExecutorService pool=Executors.newFixedThreadPool(4);
for([int i=0] i < 4 [++i])
pool.execute(new MyTask(counter));
pool.shutdown();
pool.awaitTermination(1,TimeUnit.HOURS);
}

}