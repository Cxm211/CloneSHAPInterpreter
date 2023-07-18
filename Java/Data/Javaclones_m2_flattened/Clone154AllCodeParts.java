public class Clone154AllCodePartsm2 {  
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

static void throwException (final String exClassName) throws CheckedException, UncheckedException {
Class<?> clazz;
clazz=Class.forName(exClassName);
if(CheckedException.class.isAssignableFrom(clazz))
if(UncheckedException.class.isAssignableFrom(clazz))
}

}