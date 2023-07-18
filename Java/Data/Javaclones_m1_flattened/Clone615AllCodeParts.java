public class Clone615AllCodeParts { 
public void run () {
if(bar.isDisposed() || bar.getShell().isDisposed())
return;
bar.getShell().pack(true);
orgSize[0]=bar.getShell().getSize().y;
currentSize[0]=orgSize[0];
}
 
 public void run () { 
     synchronized (lock) { 
         if (bar.isDisposed () || bar.getShell ().isDisposed ()) { 
             return; 
         } 
         currentSize [0] = bar.getShell ().getSize ().y; 
         if (currentSize [0] != orgSize [0]) { 
             return; 
         } else { 
             bar.getShell ().layout (true); 
             bar.getShell ().pack (true); 
         } 
     } 
 }

}