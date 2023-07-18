public class Clone240AllCodePartsm2 {  
 public static int solution (int X, int [] A) { 
     int [] count = new int [X]; 
     for (int i = 0; 
     i < A.length; i ++) { 
         try { 
             count [A [i] - 1] ++; 
         } catch (ArrayIndexOutOfBoundsException e) { 
         } 
         if (i >= X - 1) { 
             for (int j = 0; 
             j < count.length; j ++) { 
                 if (count [j] == 0) { 
                     break; 
                 } 
                 if (j == count.length - 1) { 
                     return i; 
                 } 
             } 
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