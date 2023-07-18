public class Clone895AllCodeParts { 
public static void main (String [] args) {
CountDownLatch latch=new CountDownLatch(1);
System.out.println("Start server");
ServerModule serverModule=new ServerModule(latch);
serverModule.start();
latch.await();
e.printStackTrace();
System.out.println("Server is done");
}
 
 public static void main (String [] args) throws InterruptedException { 
     Thread t = new Thread (() -> { 
         try { 
             Thread.sleep (5000L); 
         } catch (InterruptedException e) { 
             e.printStackTrace (); 
         } 
     }); 
     System.out.println ("Starting Server!"); 
     t.start (); 
     t.join (); 
     System.out.println ("Server is done!"); 
 }

}