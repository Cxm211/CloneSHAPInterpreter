public class Clone707AllCodeParts { 
@Override 
 public boolean equals (Object that) { 
     if (this == that) return true; 
     if (! (that instanceof People)) return false; 
     People thatPeople = (People) that; 
     return this.name.equals (thatPeople.name) && this.age == thatPeople.age; 
 } 
 
public boolean equals (Object other) {
boolean result;
if((other == null) || (getClass() != other.getClass()))
result=false;
People otherPeople=(People)other;
result=name.equals(otherPeople.name) && age == otherPeople.age;
return result;
}

}