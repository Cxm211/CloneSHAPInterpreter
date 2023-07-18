public class Clone199AllCodeParts { 
public Command deserialize (JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException {
JsonObject commandObject=json.getAsJsonObject();
JsonElement commandTypeElement=commandObject.get(commandElementName);
Class<? extends Command> commandInstanceClass=commandRegistry.get(commandTypeElement.getAsString());
Command command=gson.fromJson(json,commandInstanceClass);
return command;
}
 
 public IAnimal deserialize (JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException { 
     JsonObject jsonObject = json.getAsJsonObject (); 
     JsonPrimitive prim = (JsonPrimitive) jsonObject.get (CLASSNAME); 
     String className = prim.getAsString (); 
     Class < ? > klass = null; 
     try { 
         klass = Class.forName (className); 
     } catch (ClassNotFoundException e) { 
         e.printStackTrace (); 
         throw new JsonParseException (e.getMessage ()); 
     } 
     return context.deserialize (jsonObject.get (INSTANCE), klass); 
 }

}