public class Clone105AllCodeParts { 
private void type (char character) {
handleSpecialCharacter(character);
if(Character.isLowerCase(character))
typeCharacter(Character.toUpperCase(character));
if(Character.isUpperCase(character))
typeShiftCharacter(character);
if(Character.isDigit(character))
typeCharacter(character);
}
 
 public void type (String text) { 
     char c; 
     for (int ii = 0; 
     ii < text.length (); ii ++) { 
         c = text.charAt (ii); 
         if (c <= 31 || c == 129) { 
             pressControlKey (c); 
         } else { 
             typeAsciiCode (c); 
         } 
     } 
 }

}