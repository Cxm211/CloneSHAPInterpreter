public class Clone560AllCodeParts { 
public void actionPerformed (ActionEvent ae) {
if(ae.getSource() == select)
activeTool=SELECTION_TOOL;
if(ae.getSource() == draw)
activeTool=DRAW_TOOL;
if(ae.getSource() == text)
activeTool=TEXT_TOOL;
}
 
 public void actionPerformed (ActionEvent arg0) { 
     if (! dirty) { 
         JFileChooser ch = getFileChooser (); 
         int result = ch.showOpenDialog (gui); 
         if (result == JFileChooser.APPROVE_OPTION) { 
             try { 
                 BufferedImage bi = ImageIO.read (ch.getSelectedFile ()); 
                 setImage (bi); 
             } catch (IOException e) { 
                 showError (e); 
                 e.printStackTrace (); 
             } 
         } 
     } else { 
         JOptionPane.showMessageDialog (gui, "TODO - prompt save image.."); 
     } 
 }

}