public class Clone201AllCodePartsm2 {  
 public void mirroeView () { 
     BSTNode node = mirroeView (root); 
     preorder (node); 
     System.out.println (); 
     inorder (node); 
     System.out.println (); 
     postorder (node); 
     System.out.println (); 
 }

private BSTNode mirroeView (BSTNode node) {
if(node == null || (node.left == null && node.rigth == null))
return node;
BSTNode temp=node.left;
node.left=node.rigth;
node.rigth=temp;
mirroeView(node.left);
mirroeView(node.rigth);
return node;
}

}