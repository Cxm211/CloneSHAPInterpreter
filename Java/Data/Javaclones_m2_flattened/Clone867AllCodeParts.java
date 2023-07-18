public class Clone867AllCodePartsm2 {  
 public V put (K key, V value) { 
     readWriteLock.writeLock ().lock (); 
     V old; 
     try { 
         old = super.put (key, value); 
     } finally { 
         readWriteLock.writeLock ().unlock (); 
     } 
     return old; 
 }

public void put (Key key, Value val) {
if(map.containsKey(key))
put(key,val);
return;
while(currentSize >= maxSize)
freeSpace();
queue.add(key);
map.put(key,val);
currentSize++;
}

}