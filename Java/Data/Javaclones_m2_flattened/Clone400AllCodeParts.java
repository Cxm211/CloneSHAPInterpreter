public class Clone400AllCodeParts { 
public void contextDestroyed (ServletContextEvent servletContextEvent) { 
     if (this.driver != null) { 
         try { 
             DriverManager.deregisterDriver (driver); 
             LOG.info (String.format ("deregistering jdbc driver: %s", driver)); 
         } catch (SQLException e) { 
             LOG.warn (String.format ("Error deregistering driver %s", driver), e); 
         } 
         this.driver = null; 
     } else { 
         LOG.warn ("No driver to deregister"); 
     } 
 } 
 
public final void contextDestroyed (ServletContextEvent sce) {
ClassLoader cl=Thread.currentThread().getContextClassLoader();
Enumeration<Driver> drivers=DriverManager.getDrivers();
while(drivers.hasMoreElements())
Driver driver=drivers.nextElement();
if(driver.getClass().getClassLoader() == cl)
log.info("Deregistering JDBC driver {}",driver);
DriverManager.deregisterDriver(driver);
log.error("Error deregistering JDBC driver {}",driver,ex);
log.trace("Not deregistering JDBC driver {} as it does not belong to this webapp's ClassLoader",driver);
}

}