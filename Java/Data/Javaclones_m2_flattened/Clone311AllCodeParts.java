public class Clone311AllCodePartsm2 {  
 public static void print (Object...items) { 
     for (Object item : items) { 
         if (item.getClass ().isArray ()) { 
             Object [] objs = primitiveArrayFrom (item); 
             if (objs == null) { 
                 objs = (Object []) item; 
             } 
             for (Object obj : objs) { 
                 System.out.println (obj); 
             } 
         } else { 
             System.out.println (item); 
         } 
     } 
 }

public static void print (Object...toPrint) {
if(item.getClass() == int[].class)
System.out.println(Arrays.toString((int[])item));
if(item.getClass() == double[].class)
System.out.println(Arrays.toString((double[])item));
if(item instanceof Object[])
System.out.println(Arrays.toString((Object[])item));
System.out.println(item);
}

}