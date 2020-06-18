#include <Arduino.h>
#include <WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

const char* ssid = "RD_DVES";
const char* password = "dongvietdves";
String sendData = "";
WiFiServer wifiServer(80);
WiFiClient client;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP);
String formattedDate;
String dayStamp;
String timeStamp;
int dem =0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
  wifiServer.begin();
  


  timeClient.begin();
  timeClient.setTimeOffset(3600);
}

void loop() {
  
  while(!timeClient.update()) {
    timeClient.forceUpdate();
  }
    
  // put your main code here, to run repeatedly:
  
  client = wifiServer.available();
  if (client) {
    String s = "";
    while (client.connected()) { 
      // The formattedDate comes with the following format:
      // 2018-05-28T16:00:13Z
      // We need to extract date and time
      formattedDate = timeClient.getFormattedDate();
      //  Serial.println(formattedDate);
      int splitT = formattedDate.indexOf("T");
      dayStamp = formattedDate.substring(0, splitT);
      // Serial.print("DATE: ");
      // Serial.println(dayStamp);
      // Extract time
      timeStamp = formattedDate.substring(splitT+1, formattedDate.length()-1);
      // Serial.print("HOUR: ");
      // Serial.println(timeStamp);
      delay(100);
      dem += 10;
      sendData = "1,"+dayStamp+" " + timeStamp+", 1, s1, s2, 1=x1,2=x2,3=x3,4=x4,5=x5,6=x6,7=x7,8=x8,9="+dem+"\n";
      //client.write("1,"+dayStamp+" " + timeStamp+", ID, s1, s2, 1=x1,2=x2,3=x3,4=x4,5=x5,6=x6, ….n=xn\n");
      client.print(sendData);
      Serial.println("SEND DATA -----------------------");
      delay(5000);
      // if (client.available()>0) {
      //   char c = client.read();
      //   //client.write(c);
      //   s += c;
      // }
      // Serial.println(s);
      // s = "";
    }
 
    client.stop();
    Serial.println("Client disconnected");
 
  }
}