public class Clone19AllCodeParts { 
public void serialize (Object value, JsonGenerator jgen, SerializerProvider provider) throws IOException {
jgen.writeStartObject();
JavaType javaType=provider.constructType(CustomClass.class);
BeanDescription beanDesc=provider.getConfig().introspect(javaType);
JsonSerializer<Object> serializer=BeanSerializerFactory.instance.findBeanSerializer(provider,javaType,beanDesc);
serializer.unwrappingSerializer(null).serialize(value,jgen,provider);
jgen.writeObjectField("my_extra_field","some data");
jgen.writeEndObject();
}
 
 public void serialize (final Object bean, final JsonGenerator jgen, final SerializerProvider provider) throws IOException, JsonGenerationException { 
     jgen.writeStartObject (); 
     if (_propertyFilterId != null) { 
         serializeFieldsFiltered (bean, jgen, provider); 
     } else { 
         serializeFields (bean, jgen, provider); 
     } 
     serializerListener.postSerialization (bean, jgen); 
     jgen.writeEndObject (); 
 }

}