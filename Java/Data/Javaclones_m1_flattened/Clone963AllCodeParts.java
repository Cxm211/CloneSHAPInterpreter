public class Clone963AllCodeParts { 
public static void main (String [] args) {
int number;
Scanner in=new Scanner(System.in);
System.out.println("Enter a positive integer");
number=in.nextInt();
if(number < 0)
System.out.println("Error: Not a positive integer");
System.out.print("Convert to binary is:");
printBinaryform(number);
}
 
 public static void main (String h []) { 
     Scanner sc = new Scanner (System.in); 
     int decimal = sc.nextInt (); 
     String binary = ""; 
     if (decimal <= 0) { 
         System.out.println ("Please Enter more than 0"); 
     } else { 
         while (decimal > 0) { 
             binary = (decimal % 2) + binary; 
             decimal = decimal / 2; 
         } 
         System.out.println ("binary is:" + binary); 
     } 
 }

}