public class Clone374AllCodePartsm2 {  
 public void actionPerformed (ActionEvent evt) { 
     NewComboBox combo = (NewComboBox) evt.getSource (); 
     String selection = combo.getSelectedItem ().toString (); 
     for (int i = 0; 
     i < comboBoxes.length; i ++) { 
         NewComboBox comboI = comboBoxes [i]; 
         if (comboI != combo && comboI.getSelectedItem ().equals (selection)) { 
             comboI.setSelectedItem (combo.getPreviousSelectedItem ()); 
         } 
     } 
 }

public void actionPerformed (ActionEvent e) {
String item=(String)mainComboBox.getSelectedItem();
Object o=subItems.get(item);
if(o == null)
subComboBox.setModel(new DefaultComboBoxModel());
subComboBox.setModel(new DefaultComboBoxModel((String[])o));
}

}