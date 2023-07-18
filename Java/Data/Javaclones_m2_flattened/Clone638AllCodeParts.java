public class Clone638AllCodePartsm2 {  
 int isPerfectSquare (int n) { 
     int h = n & 0xF; 
     if (h > 9) return 0; 
     if (h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8) { 
         int t = (int) floor (sqrt ((double) n) + 0.5); 
         return t * t == n; 
     } 
     return 0; 
 }

public static boolean isPerfectSquare (long n) {
if(n < 0)
return false;
long i=(n * INV3465) >>> 52;
if(!good3465[(int)i])
return false;
long r=round(Math.sqrt(n));
return r * r == n;
return false;
}

}