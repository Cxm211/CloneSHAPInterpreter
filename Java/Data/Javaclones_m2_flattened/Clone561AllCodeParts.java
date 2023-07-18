public class Clone561AllCodePartsm2 {  
 public void actionPerformed (ActionEvent ae) { 
     if (ae.getSource () == select) { 
         activeTool = SELECTION_TOOL; 
     } else if (ae.getSource () == draw) { 
         activeTool = DRAW_TOOL; 
     } else if (ae.getSource () == text) { 
         activeTool = TEXT_TOOL; 
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