#include <Arduino.h>
#include <WiFi.h>
//#include <NTPClient.h>
//#include <WiFiUdp.h>

const char *ssid = "RD_DVES";
const char *password = "dongvietdves";
IPAddress local_IP(192, 168, 2, 244);
IPAddress gateway(192, 168, 2, 1);
IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);
IPAddress secondaryDNS(8, 8, 4, 4);

String sendData = "";
WiFiServer wifiServer(80);
//WiFiClient serverClients[2];
WiFiClient client;
TaskHandle_t blink_led;

int dem = 0, has_con, i, id;
int a;
// void blink_led_disconnect(void *pvParameters)
// {
//   for (;;)
//   {
//     // if (wifiServer.hasClient())
//     // {
//     //   serverClients[i] = wifiServer.available();
//     //   Serial.print("Client: ");
//     //   Serial.println(i);
//     //   i++;
//     //   if (i > 2)
//     //   {
//     //     i = 0;
//     //   }
//     //   has_con = 1;
//     // }

//     delay(10);
//   }
// }
void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);

  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS))
  {
    Serial.println("STA Failed to configure");
  }
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  wifiServer.begin();

  // xTaskCreatePinnedToCore(
  //     blink_led_disconnect, /* Task function. */
  //     "blink_led",          /* name of task. */
  //     1000,                 /* Stack size of task */
  //     NULL,                 /* parameter of the task */
  //     2,                    /* priority of the task */
  //     &blink_led,           /* Task handle to keep track of created task */
  //     0);                   /* pin task to core 0 */
}
void send_data()
{
  id++;
  dem += 10;
  sendData = "1,timepush,"+ String(id) +",0,s2,1=x1,2=x2,3=x3,4=x4,5=x5,6=x6,7=x7,8=x8,9=" + String(dem) + '\n';
}
void loop()
{
  
  Serial.println("Wailt Connect...");
  client = wifiServer.available();
  if (client ) {
    String s = "";
    Serial.println("CONNECTED -----------------------");
    while (client.connected())
    {
      send_data();
      client.print(sendData);
      Serial.print("Machine: ");Serial.println(id);
      Serial.print("Read Respone: ");Serial.println(client.readString());
      delay(5000);
      if(Serial.available()){
        char a = Serial.read();
        if(a == '0'){
          break;
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
    
  }
  delay(1000);
}