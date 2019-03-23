
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "d7ca9e84afc84db296eacc1c8a3ed447";
char ssid[]     = "your wifi username";
char password[] = "password";

//Other way of mentioning username and password
//char ssid[] = "raman";
//char pass[] = "raman1234";
int wifiStatus;
int connectSuccess = 0, highTime = 75, lowtime = 75;

void red() { 
      digitalWrite(D0, HIGH), delay(highTime), digitalWrite(D0, LOW), delay(lowtime);
}
void green() {
      digitalWrite(D1, HIGH), delay(highTime), digitalWrite(D1, LOW), delay(lowtime);
}
void blue() {
      digitalWrite(D2, HIGH), delay(highTime), digitalWrite(D2, LOW), delay(lowtime);
}

void setup()
{
  Serial.begin(9600);
  pinMode(D0, OUTPUT), pinMode(D1, OUTPUT), pinMode(D2, OUTPUT);
  WiFi.begin(ssid, password);
  Blynk.begin(auth, ssid, password);
}

void loop()
{
      Blynk.run();
      wifiStatus = WiFi.status();
      if(connectSuccess == 0){ blue();} 
      if(wifiStatus == WL_CONNECTED){ green(), connectSuccess ++;}
      else if(connectSuccess != 0){ red(); }
      delay(1000);
}
