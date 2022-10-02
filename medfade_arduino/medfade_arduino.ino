#include <MsTimer2.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>


String acccheck = "kr";

uint16_t BNO055_SAMPLERATE_DELAY_MS = 1;


Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);


void setup() {
  
Serial.begin(2000000);
//MsTimer2::set(1, serwrite);
//MsTimer2::start();

if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

delay(1000);

}

void loop() {
  sensors_event_t orientationData , angVelocityData , linearAccelData, magnetometerData, accelerometerData, gravityData;
  
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);
  bno.getEvent(&magnetometerData, Adafruit_BNO055::VECTOR_MAGNETOMETER);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  bno.getEvent(&gravityData, Adafruit_BNO055::VECTOR_GRAVITY);

/*
  printEvent(&orientationData);
  printEvent(&angVelocityData);
  
  printEvent(&magnetometerData);
  
  printEvent(&gravityData);
*/


  printEvent(&accelerometerData);
  printEvent(&linearAccelData);
  
  uint8_t system, gyro, accel, mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  /*
  Serial.println();
  Serial.print("Calibration: Sys=");
  Serial.print(system);
  Serial.print(" Gyro=");
  Serial.print(gyro);
  Serial.print(" Accel=");
  Serial.print(accel);
  Serial.print(" Mag=");
  Serial.println(mag);

  Serial.println("--");
  */
  delay(BNO055_SAMPLERATE_DELAY_MS);
  

}

void printEvent(sensors_event_t* event) {
  double x = -1000000, y = -1000000 , z = -1000000; //dumb values, easy to spot problem
  if (event->type == SENSOR_TYPE_ACCELEROMETER) {
    //Serial.print("linearbeschleunigung:\n");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
    acccheck = "lb";
  }
  else if (event->type == SENSOR_TYPE_ORIENTATION) {
    Serial.print("Orientierung/Winkel:\n");
    x = event->orientation.x;
    y = event->orientation.y;
    z = event->orientation.z;
  }
  else if (event->type == SENSOR_TYPE_MAGNETIC_FIELD) {
    Serial.print("Magnetometer:\n");
    x = event->magnetic.x;
    y = event->magnetic.y;
    z = event->magnetic.z;
  }
  else if (event->type == SENSOR_TYPE_GYROSCOPE) {
    Serial.print("winkelbeschleunigung:\n");
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
  }
  else if (event->type == SENSOR_TYPE_ROTATION_VECTOR) {
    Serial.print("Rot:\n");
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
  }
  else if (event->type == SENSOR_TYPE_LINEAR_ACCELERATION) {
    //Serial.print("Linearbeschleunigung korrigiert:\n");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
    acccheck = "lk";
  }
  else if (event->type == SENSOR_TYPE_GRAVITY) {
    Serial.print("Erdbeschleunigung:\n");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
  }
  else {
    Serial.print("Unk:");
  }

  size_t s = 0;
  s += Serial.print(acccheck); s += Serial.print(" ");
  s += Serial.print(x, 2); s += Serial.print(" ");
  s += Serial.print(y, 2); s += Serial.print(" ");
  s += Serial.println(z, 2);
  //Serial.print("Size: "); Serial.println(s);
}

/*
void serwrite(){
  
    
    }

    */
