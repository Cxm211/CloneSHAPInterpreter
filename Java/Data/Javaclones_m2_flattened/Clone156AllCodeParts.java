public class Clone156AllCodePartsm2 {  
 static void throwException (final String exClassName) throws CheckedException, UncheckedException { 
     Class < ? > clazz; 
     try { 
         clazz = Class.forName (exClassName); 
     } catch (ClassNotFoundException cnfe) { 
         throw new InternalError (exClassName, cnfe); 
     } 
     if (CheckedException.class.isAssignableFrom (clazz)) { 
         throw newException (clazz.asSubclass (CheckedException.class)); 
     } else if (UncheckedException.class.isAssignableFrom (clazz)) { 
         throw newException (clazz.asSubclass (UncheckedException.class)); 
     } else { 
         throw new InternalError (exClassName + " is not a valid exception"); 
     } 
 }

public static void throwException (String className) throws CheckedException, UncheckedException {
Class<?> exceptionClass;
exceptionClass=Class.forName(className);
if(CheckedException.class.isAssignableFrom(exceptionClass))
if(UncheckedException.class.isAssignableFrom(exceptionClass))
}

}