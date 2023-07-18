public class Clone911AllCodePartsm2 {  
 public static final String deriveCurveName (org.bouncycastle.jce.spec.ECParameterSpec ecParameterSpec) throws GeneralSecurityException { 
     for (@SuppressWarnings ("rawtypes") 
     Enumeration names = ECNamedCurveTable.getNames (); 
     names.hasMoreElements ();) { 
         final String name = (String) names.nextElement (); 
         final X9ECParameters params = ECNamedCurveTable.getByName (name); 
         if (params.getN ().equals (ecParameterSpec.getN ()) && params.getH ().equals (ecParameterSpec.getH ()) && params.getCurve ().equals (ecParameterSpec.getCurve ()) && params.getG ().equals (ecParameterSpec.getG ())) { 
             return name; 
         } 
     } 
     throw new GeneralSecurityException ("Could not find name for curve"); 
 }

public static final String deriveCurveName (PublicKey publicKey) throws GeneralSecurityException {
if(publicKey instanceof java.security.interfaces.ECPublicKey)
final java.security.interfaces.ECPublicKey pk=(java.security.interfaces.ECPublicKey)publicKey;
final ECParameterSpec params=pk.getParams();
return deriveCurveName(EC5Util.convertSpec(params,false));
if(publicKey instanceof org.bouncycastle.jce.interfaces.ECPublicKey)
final org.bouncycastle.jce.interfaces.ECPublicKey pk=(org.bouncycastle.jce.interfaces.ECPublicKey)publicKey;
return deriveCurveName(pk.getParameters());
}

}