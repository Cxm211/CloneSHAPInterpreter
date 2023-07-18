public class Clone557AllCodePartsm2 {  
 public void actionPerformed (ActionEvent arg0) { 
     int result = JOptionPane.OK_OPTION; 
     if (dirty) { 
         result = JOptionPane.showConfirmDialog (gui, "Erase the current painting?"); 
     } 
     if (result == JOptionPane.OK_OPTION) { 
         clear (canvasImage); 
     } 
 }

public void actionPerformed (ActionEvent arg0) {
if(!dirty)
JFileChooser ch=getFileChooser();
int result=ch.showOpenDialog(gui);
if(result == JFileChooser.APPROVE_OPTION)
BufferedImage bi=ImageIO.read(ch.getSelectedFile());
setImage(bi);
showError(e);
e.printStackTrace();
JOptionPane.showMessageDialog(gui,"TODO - prompt save image..");
}

}