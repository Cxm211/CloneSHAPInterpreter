public class Clone577AllCodePartsm2 {  
 public static int getRandomNumberBetween (int min, int max) { 
     Random foo = new Random (); 
     int randomNumber = foo.nextInt (max - min) + min; 
     if (randomNumber == min) { 
         return min + 1; 
     } else { 
         return randomNumber; 
     } 
 }

private static float getRandomNumberBetween (float numberOne, float numberTwo) throws Exception {
if(numberOne == numberTwo)
float rand=(float)Math.random();
float highRange=Math.max(numberOne,numberTwo);
float lowRange=Math.min(numberOne,numberTwo);
float lowRand=(float)Math.floor(rand - 1);
float highRand=(float)Math.ceil(rand + 1);
float genRand=(highRange - lowRange) * ((rand - lowRand) / (highRand - lowRand)) + lowRange;
return genRand;
}

}