public class Clone364AllCodeParts { 
public static int TestTryFinallyBlock () { 
     int returnValue; 
     try { 
         int i = 0; 
         i = 10; 
         returnValue = i; 
         i = 40; 
         return returnValue; 
     } catch (RuntimeException e) { 
         i = 40; 
         throw e; 
     } 
 } 
 
public static int TestTryFinallyBlock () {
int i=0;
i=10;
return i;
i=40;
System.out.println("local: " + i);
}

}