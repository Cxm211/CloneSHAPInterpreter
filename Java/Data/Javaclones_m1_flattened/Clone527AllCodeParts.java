public class Clone527AllCodeParts { 
public void refund (float balance) {
System.out.println("You have selected the refund option:");
for([int counter=(int)balance] counter >= 10 [counter-=10])
System.out.println("Balance: £" + balance);
balance-=10;
for([int counter=(int)balance] counter > 0 [counter-=1])
System.out.println("Balance: £" + balance);
balance-=1;
System.out.println("Balance: £" + balance);
}
 
 public void refund (int balance) { 
     while (balance >= 10) { 
         System.out.println ("Balance: £" + balance); 
         balance -= 10; 
     } 
     while (balance >= 0) { 
         System.out.println ("Balance: £" + balance); 
         balance -= 1; 
     } 
 }

}