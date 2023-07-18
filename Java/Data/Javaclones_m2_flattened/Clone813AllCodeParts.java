public class Clone813AllCodePartsm2 {  
 @Override 
 public boolean onKeyDown (int keyCode, KeyEvent event) { 
     if ((keyCode == KeyEvent.KEYCODE_VOLUME_DOWN)) { 
         return true; 
     } else if ((keyCode == KeyEvent.KEYCODE_VOLUME_UP)) { 
         return true; 
     } else return super.onKeyDown (keyCode, event); 
 }

public boolean onKeyDown (int keyCode, KeyEvent event) {
super.onKeyDown(keyCode,event);
if(keyCode == KeyEvent.KEYCODE_VOLUME_DOWN)
Toast.makeText(MainActivity.this,"Down working",Toast.LENGTH_SHORT).show();
return true;
return false;
}

}