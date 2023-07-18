public class Clone136AllCodeParts { 
public void onActivityResult (int requestCode, int resultCode, Intent data) { 
     super.onActivityResult (requestCode, resultCode, data); 
     if (resultCode == RESULT_OK) { 
         switch (requestCode) { 
             case SELECT_IMAGE : 
                 String imagePath = getPath (data.getData ()); 
                 Savingimagepath (imagePath); 
                 img.setImageDrawable (Drawable.createFromPath (imagePath)); 
                 break; 
         } 
     } 
 } 
 
protected void onActivityResult (int requestCode, int resultCode, Intent data) {
super.onActivityResult(requestCode,resultCode,data);
if(requestCode == IMAGE_CAPTURE && resultCode == Activity.RESULT_OK)
DBHelper dbHelper=new DBHelper(this);
SQLiteDatabase sql=dbHelper.getWritableDatabase();
sql.execSQL("insert statement for inserting path to database");
sql.close();
dbHelper.close();
}

}