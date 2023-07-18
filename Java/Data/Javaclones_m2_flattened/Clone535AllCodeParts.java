public class Clone535AllCodePartsm2 {  
 public void run () { 
     if (! isFinished ()) { 
         realRunnable.run (); 
         if (! isInfinite ()) { 
             repetitions --; 
             if (isFinished ()) { 
                 synchronized (this) { 
                     if (self == null) { 
                         try { 
                             wait (); 
                         } catch (Exception e) { 
                         } 
                     } 
                     self.cancel (false); 
                 } 
             } 
         } 
     } 
 }

public synchronized void run () {
if(!this.infinite)
if(this.repeatCounter > 0)
this.command.run();
this.repeatCounter--;
this.control.cancel(false);
this.command.run();
}

}