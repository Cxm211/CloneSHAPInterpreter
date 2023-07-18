public class Clone192AllCodeParts { 
public void actionPerformed (ActionEvent e) { 
     float newAlpha = softButton1.getAlpha () + incrementer; 
     if (newAlpha < 0) { 
         newAlpha = 0; 
         incrementer = - incrementer; 
     } else if (newAlpha > 1f) { 
         newAlpha = 1f; 
         incrementer = - incrementer; 
     } 
     softButton1.setAlpha (newAlpha); 
     softButton2.setAlpha (newAlpha); 
 } 
 
public void actionPerformed (ActionEvent e) {
UIManager.setLookAndFeel(laf[index].getClassName());
SwingUtilities.updateComponentTreeUI(frame);
exc.printStackTrace();
index=(index + 1) % laf.length;
}

}