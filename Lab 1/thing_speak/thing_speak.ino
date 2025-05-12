
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "IDEAPAD";
const char* password = "Hello144";

// REPLACE WITH THINGSPEAK.COM API KEY
String serverName = "http://api.thingspeak.com/update?api_key=UAPBC0F938YAPWRA";
// EXAMPLE -> String serverName = "http://api.thingspeak.com/update?api_key=JIOJ3DAS7F868ASD97F";
unsigned long lastTime = 0;
unsigned long timerDelay = 100;


void setup() {
  Serial.begin(115200); // Starting Serial Terminal
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

} 

void loop() {

  if ((millis() - lastTime) > timerDelay) {
    // Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
    
      String serverPath = serverName + "&field1=" + String(random(300));
      
      // Your Domain name with URL path or IP address with path
      http.begin(client, serverPath.c_str());
      
      // Send HTTP GET request
      int httpResponseCode = http.GET();
      
      if (httpResponseCode>0) {
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        String payload = http.getString();
        Serial.println(payload);
      }
      else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      // Free resources
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
}
