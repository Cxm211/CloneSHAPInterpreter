public class Clone155AllCodePartsm2 {  
 public static void throwException (final String key) throws Throwable { 
     ExceptionMapping exceptionMapping = exceptionMappings.getExceptionMappings ().get (key); 
     if (exceptionMapping != null) { 
         try { 
             Class < Throwable > exceptionClass = (Class < Throwable >) Class.forName (exceptionMapping.getClassName ()); 
             try { 
                 throw exceptionClass.cast (exceptionClass.newInstance ()); 
             } catch (InstantiationException e) { 
                 e.printStackTrace (); 
             } catch (IllegalAccessException e) { 
                 e.printStackTrace (); 
             } 
         } catch (ClassNotFoundException e) { 
             e.printStackTrace (); 
         } 
     } 
 }

public static void throwException (String className) throws CheckedException, UncheckedException {
Class<?> exceptionClass;
exceptionClass=Class.forName(className);
if(CheckedException.class.isAssignableFrom(exceptionClass))
if(UncheckedException.class.isAssignableFrom(exceptionClass))
}

}