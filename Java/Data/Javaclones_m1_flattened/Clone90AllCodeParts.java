public class Clone90AllCodeParts { 
public void type (char c) {
keyPress(VK_ALT);
keyPress(VK_NUMPAD0);
keyRelease(VK_NUMPAD0);
String altCode=Integer.toString(c);
for([int i=0] i < altCode.length() [i++])
c=(char)(altCode.charAt(i) + '0');
keyPress(c);
keyRelease(c);
keyRelease(VK_ALT);
}
 
 private void type (char character) { 
     handleSpecialCharacter (character); 
     if (Character.isLowerCase (character)) { 
         typeCharacter (Character.toUpperCase (character)); 
     } 
     if (Character.isUpperCase (character)) { 
         typeShiftCharacter (character); 
     } 
     if (Character.isDigit (character)) { 
         typeCharacter (character); 
     } 
 }

}