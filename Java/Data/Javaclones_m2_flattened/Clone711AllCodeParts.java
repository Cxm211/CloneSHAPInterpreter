public class Clone711AllCodePartsm2 {  
 public int readNumber () { 
     int x = - 1; 
     do { 
         try { 
             System.out.println ("Please enter a positive number."); 
             x = keyboard.nextInt (); 
         } catch (InputMismatchException e) { 
         } 
     } while (x < 0); 
     return x; 
 }

public int readNumber () {
int x=-1;
while(x < 0)
System.out.println("Please enter a positive number.");
x=keyboard.nextInt();
return x;
}

}