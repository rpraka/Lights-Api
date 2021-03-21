#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <Servo.h>
  
 String id = "<ID1>";
 String auth_key = "<AUTH_KEY1>";
 const int done_status = -1;
 String lights_api_base = "http://<BASE_URL>.herokuapp.com/";
 String lights_api_get = lights_api_base + "get_status/?id=" + id + "&auth_key=" + auth_key;
 String lights_api_set = lights_api_base + "set_status/?new_status=" + done_status + "&id=" + id + "&auth_key=" + auth_key;
 
 const int off_angle = 60; //Set these params
 const int on_angle = 120;
 const int rest_angle = 90;

 const char* ssid = "<SSID>";
 const char* password = "<WIFI_PASS>";

int my_angle = rest_angle;
int my_status=0;
Servo servo;

void setup () {
  servo.attach(2); //D4
  
  servo.write(rest_angle);
  
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  // Attempt to connect to Wifi network:
  Serial.print("Connecting Wifi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  IPAddress ip = WiFi.localIP();
  Serial.println(ip);
 
}
 
void loop() {
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    
    WiFiClient client;
    HTTPClient http;  //Declare HTTPClient
   
    http.begin(client, lights_api_get);  //Specify request destination
    
    int httpCode = http.GET();                                  //Send the request
    Serial.println("REQUEST SENT");
    Serial.println(httpCode);
    
    if (httpCode > 0) { //check the response code
    
    const size_t capacity = JSON_OBJECT_SIZE(1) + 30;
    DynamicJsonBuffer jsonBuffer(capacity);
    JsonObject& root = jsonBuffer.parseObject(http.getString());

    int current_status = root["current_status"];

     if (current_status != done_status) {
      //Could create more complex status triggers here
      if (current_status == 0){
        my_angle = off_angle;
      }
      if (current_status == 1){
        my_angle = on_angle;
      }
      

      servo.write(my_angle);
      delay(1000);
      servo.write(rest_angle);
      delay(1000);
      my_status = done_status;
      my_angle = rest_angle;
    
    WiFiClient post_client;
    HTTPClient post_http;
    post_http.begin(post_client, lights_api_set);  //Specify request destination
    int post_http_code = post_http.POST("None");                              
    post_http.end();
     }
    
    
    Serial.println("current_status");
    Serial.println(current_status);
    }
 
   
    http.end();
    
  }
  
  delay(500);
}
