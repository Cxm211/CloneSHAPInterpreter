public class Clone813AllCodeParts { 
public boolean onKeyDown (int keyCode, KeyEvent event) {
if((keyCode == KeyEvent.KEYCODE_VOLUME_DOWN))
return true;
if((keyCode == KeyEvent.KEYCODE_VOLUME_UP))
return true;
return super.onKeyDown(keyCode,event);
}
 
 @Override 
 public boolean onKeyDown (int keyCode, KeyEvent event) { 
     super.onKeyDown (keyCode, event); 
     if (keyCode == KeyEvent.KEYCODE_VOLUME_DOWN) { 
         Toast.makeText (MainActivity.this, "Down working", Toast.LENGTH_SHORT).show (); 
         return true; 
     } 
     return false; 
 }

}