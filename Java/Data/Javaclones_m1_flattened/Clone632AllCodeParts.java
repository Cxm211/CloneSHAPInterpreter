public class Clone632AllCodeParts { 
public static void main (String [] args) throws Exception {
Class unsafeClass=Class.forName("sun.misc.Unsafe");
Field f=unsafeClass.getDeclaredField("theUnsafe");
f.setAccessible(true);
Unsafe unsafe=(Unsafe)f.get(null);
System.out.print("4..3..2..1...");
for([] null [])
unsafe.allocateMemory(1024 * 1024);
System.out.println("Boom :)");
e.printStackTrace();
}
 
 public static void main (String [] args) throws InterruptedException { 
     while (makeMore) { 
         new Leakee (0).check (); 
     } 
     while (true) { 
         Thread.sleep (1000); 
         System.out.println ("memory=" + Runtime.getRuntime ().freeMemory () + " / " + Runtime.getRuntime ().totalMemory ()); 
     } 
 }

}