public class Clone401AllCodeParts { 
public void contextDestroyed (ServletContextEvent sce) { 
     Context initContext = new InitialContext (); 
     Context envContext = (Context) initContext.lookup ("java:/comp/env"); 
     DataSource datasource = (DataSource) envContext.lookup ("jdbc/database"); 
     try { 
         java.sql.Driver mySqlDriver = DriverManager.getDriver ("jdbc:mysql://localhost:3306/"); 
         DriverManager.deregisterDriver (mySqlDriver); 
     } catch (SQLException ex) { 
         logger.info ("Could not deregister driver:".concat (ex.getMessage ())); 
     } 
     dataSource = null; 
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