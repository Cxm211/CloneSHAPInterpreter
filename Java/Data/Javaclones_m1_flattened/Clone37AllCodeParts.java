public class Clone37AllCodeParts { 
public static void main (String args []) {
int[] solutionArray={1,2,3,4,5,6,16,15,14,13,12,11};
shuffleArray(solutionArray);
for([int i=0] i < solutionArray.length [i++])
System.out.print(solutionArray[i] + " ");
System.out.println();
}
 
 public static void main (String args []) { 
     Scanner sc = new Scanner (System.in); 
     ArrayList < Integer > l = new ArrayList < Integer > (10); 
     for (int i = 0; 
     i < 10; i ++) l.add (sc.nextInt ()); 
     Collections.shuffle (l); 
     for (int j = 0; 
     j < 10; j ++) System.out.println (l.get (j)); 
 }

}