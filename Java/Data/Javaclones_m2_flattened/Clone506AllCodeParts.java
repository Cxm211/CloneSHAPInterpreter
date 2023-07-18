public class Clone506AllCodeParts { 
public void displayImage (String strfilename, JLabel label) { 
     try { 
         BufferedImage image = ImageIO.read (new File (strfilename + ".jpg")); 
         ImageIcon icon = new ImageIcon (image); 
         label.setIcon (icon); 
     } catch (IOException | NullPointerException ex) { 
         ImageIcon icon = new ImageIcon ("NOIMAGE.jpg"); 
         label.setIcon (icon); 
     } 
 } 
 
public void displayImage (String strfilename, JLabel JLlabel) {
BufferedImage image=null;
if(!isImageExist(strfilename))
image=ImageIO.read(new File("NOIMAGE.jpg"));
image=ImageIO.read(new File(strfilename + ".jpg"));
ioe.printStackTrace();
ImageIcon icon=new ImageIcon(image);
JLlabel.setIcon(icon);
}

}