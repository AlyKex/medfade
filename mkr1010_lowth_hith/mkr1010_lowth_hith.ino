#include <MKRIMU.h>

float lin_acc, gyro_vel;

long uhTime, ohTime, sTime;

String acccheck = "abc";

float x, y, z, xgyro, ygyro, zgyro;

void setup() 
{  
  Serial.begin(2000000);

  if (!IMU.begin()) 
  {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  delay(5000);
  sTime = millis();
  Serial.println("abc");

}

void loop() 
{
  if (IMU.accelerationAvailable()) 
  {
    IMU.readAcceleration(x, y, z);
    IMU.readGyroscope(xgyro, ygyro, zgyro);
    
    lin_acc = abs(x) + abs(y) + abs(z);
    gyro_vel = abs(xgyro) + abs(ygyro) + abs(zgyro);
    
    compare(lin_acc, gyro_vel, uhTime, ohTime);
  }

  if (millis()-sTime >= 15000)
  {
  Serial.println("ex");
  exit(0);
  }
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
  
  
  
  if(lin_acc <= 3)
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
