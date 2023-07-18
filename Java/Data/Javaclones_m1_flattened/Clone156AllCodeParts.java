public class Clone156AllCodeParts { 
static void throwException (final String exClassName) throws CheckedException, UncheckedException {
Class<?> clazz;
clazz=Class.forName(exClassName);
if(CheckedException.class.isAssignableFrom(clazz))
if(UncheckedException.class.isAssignableFrom(clazz))
}
 
 public static void throwException (String className) throws CheckedException, UncheckedException { 
     Class < ? > exceptionClass; 
     try { 
         exceptionClass = Class.forName (className); 
     } catch (ClassNotFoundException e) { 
         throw new IllegalArgumentException (e); 
     } 
     try { 
         if (CheckedException.class.isAssignableFrom (exceptionClass)) { 
             throw exceptionClass.asSubclass (CheckedException.class).newInstance (); 
         } else if (UncheckedException.class.isAssignableFrom (exceptionClass)) { 
             throw exceptionClass.asSubclass (UncheckedException.class).newInstance (); 
         } else { 
             throw new IllegalArgumentException ("Not a valid exception type: " + exceptionClass.getName ()); 
         } 
     } catch (InstantiationException | IllegalAccessException e) { 
         throw new IllegalStateException (e); 
     } 
 }

}