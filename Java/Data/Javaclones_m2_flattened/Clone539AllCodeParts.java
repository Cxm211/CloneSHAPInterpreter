public class Clone539AllCodePartsm2 {  
 public String nthShortWord (String [] words, int n) { 
     int nthShortWord = 0; 
     for (int i = 0; 
     i < words.length; i ++) { 
         if (words [i].length () <= 3) nthShortWord ++; 
         if (nthShortWord == n) return words [i]; 
     } 
     return ""; 
 }

public String nthShortWord (String [] words, int n) {
int nthShortWord=0;
String shortWord="notFound";
for([int i=0] i < words.length [i++])
if(words[i].length() <= 3)
nthShortWord++;
if(nthShortWord == n)
shortWord=nthShortWord[i];
return shortWord;
}

}