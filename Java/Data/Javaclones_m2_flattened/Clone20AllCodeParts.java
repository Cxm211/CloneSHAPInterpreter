public class Clone20AllCodeParts { 
@Override 
 public void serialize (Test value, JsonGenerator jgen, SerializerProvider provider) throws IOException, JsonProcessingException { 
     jgen.writeStartObject (); 
     Field [] fields = value.getClass ().getDeclaredFields (); 
     for (Field field : fields) { 
         try { 
             jgen.writeObjectField (field.getName (), field.get (value)); 
         } catch (IllegalArgumentException | IllegalAccessException e) { 
             e.printStackTrace (); 
         } 
     } 
     jgen.writeObjectField ("extra_field", "whatever_value"); 
     jgen.writeEndObject (); 
 } 
 
public void serialize (final Object bean, final JsonGenerator jgen, final SerializerProvider provider) throws IOException, JsonGenerationException {
jgen.writeStartObject();
if(_propertyFilterId != null)
serializeFieldsFiltered(bean,jgen,provider);
serializeFields(bean,jgen,provider);
serializerListener.postSerialization(bean,jgen);
jgen.writeEndObject();
}

}