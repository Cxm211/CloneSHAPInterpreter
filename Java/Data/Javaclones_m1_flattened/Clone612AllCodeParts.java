public class Clone612AllCodeParts { 
public static void main (String [] args) throws IOException {
Process p=Runtime.getRuntime().exec(XVFB_COMMAND);
FirefoxBinary firefox=new FirefoxBinary();
firefox.setEnvironmentProperty("DISPLAY",":" + DISPLAY_NUMBER);
WebDriver driver=new FirefoxDriver(firefox,null);
driver.get(URL);
File scrFile=((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
FileUtils.copyFile(scrFile,new File(RESULT_FILENAME));
driver.close();
p.destroy();
}
 
 public static void main (String [] args) { 
     try { 
         Robot robot = new Robot (); 
         BufferedImage bi = robot.createScreenCapture (new Rectangle (Toolkit.getDefaultToolkit ().getScreenSize ())); 
         ImageIO.write (bi, "jpg", new File ("C:/imageTest.jpg")); 
     } catch (AWTException e) { 
         e.printStackTrace (); 
     } catch (IOException e) { 
         e.printStackTrace (); 
     } 
 }

}