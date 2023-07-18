public class Clone327AllCodeParts { 
public void mouseMoved (MouseEvent e) {
int x=width / 2;
int y=height / 2;
Point mousePoint=e.getPoint();
int deltaX=mousePoint.x - x;
int deltaY=mousePoint.y - y;
polyrot=-Math.atan2(deltaX,deltaY);
polyrot=Math.toDegrees(polyrot) + 180;
repaint();
}
 
 public void mouseMoved (MouseEvent e) { 
     xpos = getX (); 
     if (xpos < 0) { 
         polyrot --; 
     } else if (xpos > 0) { 
         polyrot ++; 
     } 
     repaint (); 
     break; 
 }

}