public class Clone738AllCodePartsm2 {  
 public int read () throws IOException { 
     if (currentPos < currentLineEnd) { 
         in.seek (currentPos ++); 
         int readByte = in.readByte (); 
         return readByte; 
     } else if (currentPos < 0) { 
         return - 1; 
     } else { 
         findPrevLine (); 
         return read (); 
     } 
 }

public int read () throws IOException {
if(currentFilePos <= 0 && currentBufferPos < 0 && currentLineReadPos < 0)
return -1;
if(!lineBuffered)
fillLineBuffer();
if(lineBuffered)
if(currentLineReadPos == 0)
lineBuffered=false;
return currentLine[currentLineReadPos--];
return 0;
}

}