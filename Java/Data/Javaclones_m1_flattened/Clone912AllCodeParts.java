public class Clone912AllCodeParts { 
public static final String deriveCurveName (org.bouncycastle.jce.spec.ECParameterSpec ecParameterSpec) throws GeneralSecurityException {
for([@SuppressWarnings("rawtypes") Enumeration names=ECNamedCurveTable.getNames()] names.hasMoreElements() [])
final String name=(String)names.nextElement();
final X9ECParameters params=ECNamedCurveTable.getByName(name);
if(params.getN().equals(ecParameterSpec.getN()) && params.getH().equals(ecParameterSpec.getH()) && params.getCurve().equals(ecParameterSpec.getCurve())&& params.getG().equals(ecParameterSpec.getG()))
return name;
}
 
 public static final String deriveCurveName (PrivateKey privateKey) throws GeneralSecurityException { 
     if (privateKey instanceof java.security.interfaces.ECPrivateKey) { 
         final java.security.interfaces.ECPrivateKey pk = (java.security.interfaces.ECPrivateKey) privateKey; 
         final ECParameterSpec params = pk.getParams (); 
         return deriveCurveName (EC5Util.convertSpec (params, false)); 
     } else if (privateKey instanceof org.bouncycastle.jce.interfaces.ECPrivateKey) { 
         final org.bouncycastle.jce.interfaces.ECPrivateKey pk = (org.bouncycastle.jce.interfaces.ECPrivateKey) privateKey; 
         return deriveCurveName (pk.getParameters ()); 
     } else throw new IllegalArgumentException ("Can only be used with instances of ECPrivateKey (either jce or bc implementation)"); 
 }

}