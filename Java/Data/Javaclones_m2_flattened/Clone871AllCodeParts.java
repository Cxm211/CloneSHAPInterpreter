public class Clone871AllCodePartsm2 {  
 public void put (K key, V val) { 
     while (currentSize >= maxSize) { 
         freeSpace (); 
     } 
     if (map.containsKey (key)) { 
         get (key); 
         return; 
     } 
     ListNode < K > ln = queue.add (key); 
     ValueHolder < K, V > rv = new ValueHolder < K, V > (val, ln); 
     map.put (key, rv); 
     currentSize ++; 
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