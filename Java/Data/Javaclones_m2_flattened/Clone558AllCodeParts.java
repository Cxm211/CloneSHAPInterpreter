public class Clone558AllCodePartsm2 {  
 public void actionPerformed (ActionEvent arg0) { 
     int result = JOptionPane.OK_OPTION; 
     if (dirty) { 
         result = JOptionPane.showConfirmDialog (gui, "Erase the current painting?"); 
     } 
     if (result == JOptionPane.OK_OPTION) { 
         clear (canvasImage); 
     } 
 }

public void actionPerformed (ActionEvent e) {
JFileChooser ch=getFileChooser();
int result=ch.showSaveDialog(gui);
if(result == JFileChooser.APPROVE_OPTION)
File f=ch.getSelectedFile();
ImageIO.write(BasicPaint.this.canvasImage,"png",f);
BasicPaint.this.originalImage=BasicPaint.this.canvasImage;
dirty=false;
showError(ioe);
ioe.printStackTrace();
}

}