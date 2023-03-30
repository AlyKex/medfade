#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <MsTimer2.h>
#include "Adafruit_FONA.h"
#include "Secrets.h"
#include "Fona.h"
#include "BNO055.h"

#if (defined(__AVR__) || defined(ESP8266)) && !defined(__AVR_ATmega2560__)

#include <SoftwareSerial.h>

SoftwareSerial fonaSS = SoftwareSerial(SECRET_TX, SECRET_RX);
SoftwareSerial *fonaSerial = &fonaSS;
#else
HardwareSerial *fonaSerial = &Serial1;
#endif

Adafruit_FONA fona = Adafruit_FONA(SECRET_RST);


bool fallstate = false;
long uhTime, ohTime, sTime;

String acccheck = "abc";

double lin_acc, gyro_vel;

int i = 1;

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);


void setup() {

  Serial.begin(SECRET_BAUD);
  Serial.println(F("FONA basic test"));
  Serial.println(F("Initializing....(May take 3 seconds)"));

  fonaSerial->begin(SECRET_FBAUD);
  if (!fona.begin(*fonaSerial)) {
    Serial.println(F("Couldn't find FONA"));
    while (1)
      ;
  }


if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  FonaStartUp(fona);

  delay(2000);
  sTime = millis();
  Serial.println("abc");

  

  MsTimer2::set(10, accw);
  MsTimer2::start(); 


  
}

void loop() {


  if(i == 1){
    
  sensors_event_t angVelocityData ,accelerometerData;

  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);

  gyro_vel = printEvent(&angVelocityData);
  lin_acc = printEvent(&accelerometerData);


  compare(lin_acc, gyro_vel, uhTime, ohTime);
  

  i = 0;
  }

  /*
  if (millis()-sTime >= 15000)
  {
  Serial.println("ex");
  exit(0);
  }
*/

  


}

double printEvent(sensors_event_t* event) {
  double x = -1000000, y = -1000000 , z = -1000000; //default values --> fehler leicht erkennen
  double absval = 0;
  
  if (event->type == SENSOR_TYPE_ACCELEROMETER) {
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
    absval = abs(x) + abs(y) + abs(z);
  }

    else if (event->type == SENSOR_TYPE_GYROSCOPE) {
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
    absval = abs(x*57.3) + abs(y*57.3) + abs(z*57.3);
  }

  
  return absval;
}

void accw()
{
  i = 1;
}

void compare(double lin_acc, long gyro_vel, long &uhTime, long &ohTime)
{
  /*Ausgabe von Überprüfwerten
  Serial.print(lin_acc);
  Serial.print(" ");
  Serial.println(gyro_vel);
  */
  
  
  if(lin_acc <= 28)
  {
    uhTime = millis();
  }
 
  unsigned long tTime = millis();
  if (lin_acc >= 60 && tTime - uhTime <= 200)
  {
    ohTime = millis();
    
    if(gyro_vel >= 200)
    {
          SendFall(fona);
    }

      
  }
}
