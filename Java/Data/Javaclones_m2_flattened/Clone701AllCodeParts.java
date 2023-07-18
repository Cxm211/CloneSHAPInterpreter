public class Clone701AllCodePartsm2 {  
 public static void printTable (String [] countries, int [] populations) { 
     int countryLength = 0; 
     long populationLength = 0; 
     for (String country : countries) { 
         if (country.length () > countryLength) countryLength = country.length (); 
     } 
     for (int i : populations) { 
         if (String.valueOf (i).length () > populationLength) populationLength = String.valueOf (i).length (); 
     } 
     for (int i = 0; 
     i < countries.length; i ++) System.out.format ("%-" + (countryLength + 1) + "s|%" + (populationLength + 1) + "d\n", countries [i], populations [i]); 
 }

public static void printTable (String [] countries, int [] populations) {
if(countries.length == 0 || populations.length == 0 || countries.length != populations.length)
return;
int longestCountry=Arrays.stream(countries).map(null).mapToInt(null).max().getAsInt();
int longestPop=Arrays.stream(populations).mapToObj(null).mapToInt(null).max().getAsInt();
for([int i=0] i < countries.length [i++])
System.out.printf("%-" + longestCountry + "s | %"+ longestPop+ "d%n",countries[i],populations[i]);
}

}