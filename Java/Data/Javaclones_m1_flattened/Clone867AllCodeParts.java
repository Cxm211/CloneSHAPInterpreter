public class Clone867AllCodeParts { 
public V put (K key, V value) {
readWriteLock.writeLock().lock();
V old;
old=super.put(key,value);
readWriteLock.writeLock().unlock();
return old;
}
 
 public void put (Key key, Value val) { 
     if (map.containsKey (key)) { 
         put (key, val); 
         return; 
     } 
     while (currentSize >= maxSize) { 
         freeSpace (); 
     } 
     synchronized (this) { 
         queue.add (key); 
         map.put (key, val); 
         currentSize ++; 
     } 
 }

}