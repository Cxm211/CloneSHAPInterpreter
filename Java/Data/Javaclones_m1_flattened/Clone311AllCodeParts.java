public class Clone311AllCodeParts { 
public static void print (Object...items) {
if(item.getClass().isArray())
Object[] objs=primitiveArrayFrom(item);
if(objs == null)
objs=(Object[])item;
System.out.println(obj);
System.out.println(item);
}
 
 public static void print (Object...toPrint) { 
     for (Object item : toPrint) { 
         if (item.getClass () == int [].class) { 
             System.out.println (Arrays.toString ((int []) item)); 
         } else if (item.getClass () == double [].class) { 
             System.out.println (Arrays.toString ((double []) item)); 
         } else if (item instanceof Object []) { 
             System.out.println (Arrays.toString ((Object []) item)); 
         } else { 
             System.out.println (item); 
         } 
     } 
 }

}