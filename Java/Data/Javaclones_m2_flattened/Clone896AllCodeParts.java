public class Clone896AllCodeParts { 
public boolean onOptionsItemSelected (MenuItem item) { 
     switch (item.getItemId ()) { 
         case android.R.id.home : 
             NavUtils.navigateUpFromSameTask (this); 
             return true; 
         default : 
             return super.onOptionsItemSelected (item); 
     } 
 } 
 
public boolean onOptionsItemSelected (MenuItem item) {
if(getParentActivityIntent() == null)
Log.i(TAG,"You have forgotten to specify the parentActivityName in the AndroidManifest!");
onBackPressed();
NavUtils.navigateUpFromSameTask(this);
return true;
return super.onOptionsItemSelected(item);
}

}