public class Clone364AllCodeParts { 
public static int TestTryFinallyBlock () {
int returnValue;
int i=0;
i=10;
returnValue=i;
i=40;
return returnValue;
i=40;
}
 
 public static int TestTryFinallyBlock () { 
     int i = 0; 
     try { 
         i = 10; 
         return i; 
     } finally { 
         i = 40; 
         System.out.println ("local: " + i); 
     } 
 }

}