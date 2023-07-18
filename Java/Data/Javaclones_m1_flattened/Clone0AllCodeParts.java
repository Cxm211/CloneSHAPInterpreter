public class Clone0AllCodeParts { 
public static BufferedImage scale (BufferedImage imageToScale, int dWidth, int dHeight) {
BufferedImage scaledImage=null;
if(imageToScale != null)
scaledImage=new BufferedImage(dWidth,dHeight,imageToScale.getType());
Graphics2D graphics2D=scaledImage.createGraphics();
graphics2D.drawImage(imageToScale,0,0,dWidth,dHeight,null);
graphics2D.dispose();
return scaledImage;
}
 
 public static BufferedImage scale (BufferedImage sbi, int imageType, int dWidth, int dHeight, double fWidth, double fHeight) { 
     BufferedImage dbi = null; 
     if (sbi != null) { 
         dbi = new BufferedImage (dWidth, dHeight, imageType); 
         Graphics2D g = dbi.createGraphics (); 
         AffineTransform at = AffineTransform.getScaleInstance (fWidth, fHeight); 
         g.drawRenderedImage (sbi, at); 
     } 
     return dbi; 
 }

}