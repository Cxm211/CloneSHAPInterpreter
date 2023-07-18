public class Clone934AllCodeParts { 
public static void listFilesForFolder (final File folder) { 
     for (final File fileEntry : folder.listFiles ()) { 
         if (fileEntry.isDirectory ()) { 
             listFilesForFolder (fileEntry); 
         } else { 
             if (fileEntry.isFile ()) { 
                 temp = fileEntry.getName (); 
                 if ((temp.substring (temp.lastIndexOf ('.') + 1, temp.length ()).toLowerCase ()).equals ("txt")) System.out.println ("File= " + folder.getAbsolutePath () + "\\" + fileEntry.getName ()); 
             } 
         } 
     } 
 } 
 
public static void listFilesForFolder (final File folder) {
if(fileEntry.isDirectory())
listFilesForFolder(fileEntry);
System.out.println(fileEntry.getName());
}

}