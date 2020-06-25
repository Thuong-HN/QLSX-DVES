#include <Arduino.h>
#include <WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

const char* ssid = "RD_DVES";
const char* password = "dongvietdves";
IPAddress local_IP(192, 168, 2, 244);
IPAddress gateway(192, 168, 2, 1);
IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);   
IPAddress secondaryDNS(8, 8, 4, 4); 

String sendData = "";
WiFiServer wifiServer(80);
WiFiClient serverClients[20];
TaskHandle_t blink_led;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP);
String formattedDate;
String dayStamp;
String timeStamp;
int dem =0, has_con, i;
void blink_led_disconnect( void * pvParameters ){
  for(;;){
    if (wifiServer.hasClient()) {
    
      i++;
      if (!serverClients[i].connected()) { // equivalent to !serverClients[i].connected()
        serverClients[i] = wifiServer.available();
        Serial.print("NEW client: ");Serial.println(i);
        has_con = 1;
        
      }
    
  }
    delay(1);
  } 
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
 
  delay(1000);
 
  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
    Serial.println("STA Failed to configure");
  }
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  wifiServer.begin();
  


  timeClient.begin();
  timeClient.setTimeOffset(3600);


  xTaskCreatePinnedToCore(
                    blink_led_disconnect,   /* Task function. */
                    "blink_led",     /* name of task. */
                    1000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    0,           /* priority of the task */
                    &blink_led,      /* Task handle to keep track of created task */
                    0);          /* pin task to core 0 */
}
void send_data(){
  formattedDate = timeClient.getFormattedDate();
        int splitT = formattedDate.indexOf("T");
        dayStamp = formattedDate.substring(0, splitT);
        timeStamp = formattedDate.substring(splitT+1, formattedDate.length()-1);
        
        dem += 10;
        sendData = "1,"+dayStamp+" " + timeStamp+", 1, s1, s2, 1=x1,2=x2,3=x3,4=x4,5=x5,6=x6,7=x7,8=x8,9="+dem+"\n";
}
void loop() {
  
  while(!timeClient.update()) {
    timeClient.forceUpdate();
  } 
  if(serverClients[i].available()){
    while(serverClients[i].connected())
      {
        send_data();
        delay(3000);
        if(has_con == 1){
          has_con = 0;
          break;
        }
        
      }
  }
      
      
  
    

  // WiFiClient client = wifiServer.available();
  // if (client ) {
  //   String s = "";
  //   while (client.connected()) 
  //   { 
  //     formattedDate = timeClient.getFormattedDate();
  //     int splitT = formattedDate.indexOf("T");
  //     dayStamp = formattedDate.substring(0, splitT);
  //     timeStamp = formattedDate.substring(splitT+1, formattedDate.length()-1);
  //     delay(100);
  //     dem += 10;
  //     sendData = "1,"+dayStamp+" " + timeStamp+", 1, s1, s2, 1=x1,2=x2,3=x3,4=x4,5=x5,6=x6,7=x7,8=x8,9="+dem+"\n";
  //     client.print(sendData);
  //     
  //     Serial.println("SEND DATA -----------------------");
  //     delay(3000);
  //     if(Serial.available()){
  //       char a = Serial.read();
  //       if(a == '0'){
  //         client.stop();
  //       }
  //     }
  //   }
  //   else{
  //       client.stop();client1.stop();
  //       Serial.println("Client disconnected");
  //   }
    
 
  // }
}