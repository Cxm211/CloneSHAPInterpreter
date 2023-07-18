public class Clone154AllCodeParts { 
public static void throwException (final String key) throws Throwable {
ExceptionMapping exceptionMapping=exceptionMappings.getExceptionMappings().get(key);
if(exceptionMapping != null)
Class<Throwable> exceptionClass=(Class<Throwable>)Class.forName(exceptionMapping.getClassName());
e.printStackTrace();
e.printStackTrace();
e.printStackTrace();
}
 
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

}