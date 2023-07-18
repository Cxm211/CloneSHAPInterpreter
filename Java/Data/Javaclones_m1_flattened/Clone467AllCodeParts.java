public class Clone467AllCodeParts { 
public static void main (String args []) throws IOException {
JavaPingExampleProgram ping=new JavaPingExampleProgram();
List<String> commands=new ArrayList<String>();
commands.add("ping");
commands.add("-c");
commands.add("5");
commands.add("74.125.236.73");
ping.doCommand(commands);
}
 
 public static void main (String [] args) { 
     try { 
         InetAddress address = InetAddress.getByName ("192.168.1.103"); 
         boolean reachable = address.isReachable (10000); 
         System.out.println ("Is host reachable? " + reachable); 
     } catch (Exception e) { 
         e.printStackTrace (); 
     } 
 }

}