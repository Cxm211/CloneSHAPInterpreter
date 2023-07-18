public class Clone261AllCodePartsm2 {  
 public int solution (final int X, final int [] A) { 
     Set < Integer > emptyPosition = new HashSet < Integer > (); 
     for (int i = 1; 
     i <= X; i ++) { 
         emptyPosition.add (i); 
     } 
     for (int i = 0; 
     i < A.length; i ++) { 
         emptyPosition.remove (A [i]); 
         if (emptyPosition.size () == 0) { 
             return i; 
         } 
     } 
     return - 1; 
 }

public int solution (int X, int [] A) {
Set<Integer> leaves=new HashSet<>();
for([int i=0] i < A.length [i++])
leaves.add(A[i]);
if(leaves.contains(X) && leaves.size() == X)
return i;
return -1;
}

}