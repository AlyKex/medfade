#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <MsTimer2.h>



long uhTime, ohTime, sTime;

String acccheck = "abc";

double lin_acc, gyro_vel;

int i = 1;

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);


void setup() {

   pinMode(12, OUTPUT);

  


    
Serial.begin(2000000);

if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

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
  
  if (millis()-sTime >= 15000)
  {
  Serial.println("ex");
  exit(0);
  }


  


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
  Serial.print(45);
  Serial.print(" ");
  Serial.println(3);
  */
  Serial.print(lin_acc);
  Serial.print(" ");
  Serial.println(gyro_vel);
  
  
  
  if(lin_acc <= 1.8)
  {
    //Serial.println(" untereracc threshhold erreicht");
    uhTime = millis();
  }
  
  unsigned long tTime = millis();
  if (lin_acc >= 45 && tTime - uhTime <= 500)
  {
    //Serial.println("oberer threshold erreicht");
    ohTime = millis();
    
    if(gyro_vel >= 300)
    {
      //Serial.println("sturz erkannt");
    }

      
  }
}
