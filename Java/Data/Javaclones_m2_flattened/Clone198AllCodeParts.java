public class Clone198AllCodePartsm2 {  
 public Command deserialize (JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException { 
     try { 
         JsonObject commandObject = json.getAsJsonObject (); 
         JsonElement commandTypeElement = commandObject.get (commandElementName); 
         Class < ? extends Command > commandInstanceClass = commandRegistry.get (commandTypeElement.getAsString ()); 
         Command command = gson.fromJson (json, commandInstanceClass); 
         return command; 
     } catch (Exception e) { 
         throw new RuntimeException (e); 
     } 
 }

public IAnimal deserialize (JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException {
JsonObject jsonObject=json.getAsJsonObject();
JsonPrimitive prim=(JsonPrimitive)jsonObject.get(CLASSNAME);
String className=prim.getAsString();
Class<?> klass=null;
klass=Class.forName(className);
e.printStackTrace();
return context.deserialize(jsonObject.get(INSTANCE),klass);
}

}