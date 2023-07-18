public class Clone560AllCodePartsm2 {  
 public void actionPerformed (ActionEvent ae) { 
     if (ae.getSource () == select) { 
         activeTool = SELECTION_TOOL; 
     } else if (ae.getSource () == draw) { 
         activeTool = DRAW_TOOL; 
     } else if (ae.getSource () == text) { 
         activeTool = TEXT_TOOL; 
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