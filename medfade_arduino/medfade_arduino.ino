#include <MsTimer2.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>


String acccheck = "kr";

uint16_t BNO055_SAMPLERATE_DELAY_MS = 10 ;


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

while(true){
     uint8_t system, gyro, accel, mag = 0;
     bno.getCalibration(&system, &gyro, &accel, &mag);
     if (system == 3){
      digitalWrite(12, HIGH);
      delay(1000);
      digitalWrite(12,LOW);
      break;
     }
}
 
  

delay(1000);

}

void loop() {
  sensors_event_t orientationData , angVelocityData , linearAccelData, accelerometerData;
  
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);

  printEvent(&orientationData);
  printEvent(&accelerometerData);
  printEvent(&linearAccelData);

  delay(BNO055_SAMPLERATE_DELAY_MS);

}

void printEvent(sensors_event_t* event) {
  double x = -1000000, y = -1000000 , z = -1000000; //default values --> fehler leicht erkennen
  if (event->type == SENSOR_TYPE_ACCELEROMETER) {
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
    acccheck = "lb"; //linear beschleunigung (nicht korrigiert)
  }
  else if (event->type == SENSOR_TYPE_ORIENTATION) {
    x = event->orientation.x;
    y = event->orientation.y;
    z = event->orientation.z;
    acccheck = "ow"; //orientierung in grad (winkel)
  }
  else if (event->type == SENSOR_TYPE_LINEAR_ACCELERATION) {
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
    acccheck = "lk"; //linear beschleunigung korrigiert
  }

  Serial.print(acccheck);Serial.print(" ");
  Serial.print(x, 2); Serial.print(" ");
  Serial.print(y, 2); Serial.print(" ");
  Serial.println(z, 2);
}
