public class Clone852AllCodeParts { 
public static void main (String [] args) throws Exception {
DocumentBuilderFactory dbf=DocumentBuilderFactory.newInstance();
DocumentBuilder db=dbf.newDocumentBuilder();
Document document=db.parse(new File("input.xml"));
NodeList nodeList=document.getElementsByTagName("Item");
for([int x=0, size=nodeList.getLength()] x < size [x++])
System.out.println(nodeList.item(x).getAttributes().getNamedItem("name").getNodeValue());
}
 
 public static void main (String [] s) throws VTDException { 
     VTDGen vg = new VTDGen (); 
     if (! vg.parseFile ("input.xml", false)) return; 
     VTDNav vn = vg.getNav (); 
     AutoPilot ap = new AutoPilot (vn); 
     ap.selectXPath ("/xml/item/@name"); 
     int i = 0; 
     while ((i = ap.evalXPath ()) != - 1) { 
         System.out.println (" item name is ===>" + vn.toString (i + 1)); 
     } 
 }

}