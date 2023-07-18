public class Clone793AllCodeParts { 
public static void main (String args []) {
String[] arr={"foo:1,2,3","bar:a,b","baz:5,6,7"};
CartesianProductLHM cp=new CartesianProductLHM(arr);
List<List<String>> lls=cp.allUniqueCombinations();
System.out.print(s + "\t");
System.out.println();
}
 
 public static void main (String [] args) { 
     LinkedHashMap < String, Vector < String > > data = new LinkedHashMap < String, Vector < String > > (); 
     data.put ("foo", new Vector < String > (Arrays.asList ("1", "2", "3"))); 
     data.put ("bar", new Vector < String > (Arrays.asList ("3", "2"))); 
     data.put ("baz", new Vector < String > (Arrays.asList ("5", "6", "7"))); 
     Foo foo = new Foo (data); 
     for (String [] combination : foo.allUniqueCombinations ()) { 
         System.out.println (Arrays.toString (combination)); 
     } 
 }

}