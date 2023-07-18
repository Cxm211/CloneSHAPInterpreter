public class Clone608AllCodeParts { 
public static void main (String args []) {
inp=new Scanner(System.in);
String str=inp.nextLine();
List<Character> arrlist=new ArrayList<Character>();
for([int i=0] i < str.length() [i++])
arrlist.add(str.charAt(i));
for([int i=0] i < str.length() [i++])
int freq=Collections.frequency(arrlist,str.charAt(i));
System.out.println("Frequency of " + str.charAt(i) + "  is:   "+ freq);
}
 
 public static void main (String [] args) { 
     String output = ""; 
     Multiset < String > wordsMultiset = HashMultiset.create (); 
     String [] words = "AAABBBBCC".split (""); 
     wordsMultiset.addAll (Arrays.asList (words)); 
     for (Entry < String > string : wordsMultiset.entrySet ()) { 
         if (! string.getElement ().isEmpty ()) output += string.getCount () + "" + string.getElement (); 
     } 
     System.out.println (output); 
 }

}