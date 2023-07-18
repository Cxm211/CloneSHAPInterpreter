public class Clone938AllCodePartsm2 {  
 public String join (String a, String b, String separator) { 
     if (! isEmpty (a) && ! isEmpty (b)) { 
         return a + separator + b; 
     } 
     if (! isEmpty (a)) { 
         return a; 
     } 
     if (! isEmpty (b)) { 
         return b; 
     } 
     return ""; 
 }

private static String join (String delimiter, String...parts) {
StringBuilder builder=new StringBuilder();
if(!isEmpty(part))
if(builder.length() > 0)
builder.append(delimiter);
builder.append(part);
return builder.toString();
}

}