public class Clone589AllCodeParts { 
public static void main (String [] args) throws TwilioRestException {
TwilioRestClient client=new TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN);
List<NameValuePair> params=new ArrayList<NameValuePair>();
params.add(new BasicNameValuePair("Body","Test Twilio message"));
params.add(new BasicNameValuePair("To","+14159352345"));
params.add(new BasicNameValuePair("From","+14158141829"));
MessageFactory messageFactory=client.getAccount().getMessageFactory();
Message message=messageFactory.create(params);
System.out.println(message.getSid());
}
 
 public static void main (String [] args) throws Exception { 
     AuthMethod auth = new TokenAuthMethod (API_KEY, API_SECRET); 
     NexmoClient client = new NexmoClient (auth); 
     TextMessage message = new TextMessage (FROM_NUMBER, TO_NUMBER, "Hello from Nexmo!"); 
     SmsSubmissionResult [] responses = client.getSmsClient ().submitMessage (message); 
     for (SmsSubmissionResult response : responses) { 
         System.out.println (response); 
     } 
 }

}