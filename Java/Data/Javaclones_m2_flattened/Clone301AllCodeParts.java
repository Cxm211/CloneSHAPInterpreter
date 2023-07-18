public class Clone301AllCodePartsm2 {  
 private static int solution (int N) { 
     int gap = 0; 
     String binaryStr = Integer.toBinaryString (N); 
     String [] zeroArrays = binaryStr.split ("1"); 
     System.out.println (Arrays.toString (zeroArrays)); 
     for (String zeroArray : zeroArrays) { 
         gap = zeroArray.length () > gap ? zeroArray.length () : gap; 
     } 
     return gap; 
 }

public int solution (int N) {
int result=0;
while(N > 0)
if((N & 1) == 1)
int temp=0;
while((N>>=1) > 0 && ((N & 1) != 1))
temp++;
result=Math.max(result,temp);
N>>=1;
return result;
}

}