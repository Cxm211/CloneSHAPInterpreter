public class Clone535AllCodeParts { 
public void run () {
if(!isFinished())
realRunnable.run();
if(!isInfinite())
repetitions--;
if(isFinished())
if(self == null)
wait();
self.cancel(false);
}
 
 public synchronized void run () { 
     if (! this.infinite) { 
         if (this.repeatCounter > 0) { 
             this.command.run (); 
             this.repeatCounter --; 
         } else { 
             this.control.cancel (false); 
         } 
     } else { 
         this.command.run (); 
     } 
 }

}