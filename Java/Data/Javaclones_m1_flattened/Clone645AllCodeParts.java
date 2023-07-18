public class Clone645AllCodeParts { 
public static void main (final String...args) {
if(args.length == 0)
final Pattern pattern=Pattern.compile(args[0]);
final Charset cs=Charset.defaultCharset();
final CharsetDecoder decoder=cs.newDecoder().onMalformedInput(CodingErrorAction.REPORT);
String line;
while((line=reader.readLine()) != null)
if(pattern.matcher(line).find())
System.out.println(line);
}
 
 public static void main (String [] args) throws FileNotFoundException { 
     String s = "this is line one\n" + "this is line two\n" + "This is line three"; 
     Pattern p = Pattern.compile ("this"); 
     Scanner scanner = new Scanner (s); 
     while (scanner.hasNextLine ()) { 
         String line = scanner.nextLine (); 
         Matcher m = p.matcher (line); 
         if (m.find ()) { 
             System.out.println (line); 
         } 
     } 
 }

}