#include <MKRIMU.h>

float lin_acc, gyro_vel;

long uhTime, ohTime, sTime;

String acccheck = "abc";

float hrp[6];

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
  standard(hrp);
 sTime = millis();
 Serial.println("start");
}

void loop() 
{
  if (IMU.accelerationAvailable()) 
  {
    IMU.readAcceleration(x, y, z);
    IMU.readGyroscope(xgyro, ygyro, zgyro);
    IMU.readEulerAngles(hrp[3], hrp[4], hrp[5]);

    lin_acc = abs(x) + abs(y) + abs(z);
    gyro_vel = abs(xgyro) + abs(ygyro) + abs(zgyro);
    
    compare(lin_acc, gyro_vel, uhTime, ohTime, hrp);
  }
  
  /*
  if (millis()-sTime >= 15000)
  {
  Serial.println("ex");
  exit(0);
  }
  */
  
}


void compare(double lin_acc, long gyro_vel, long &uhTime, long &ohTime, float *hrp)
{
  /*Ausgabe von Überprüfwerten
  Serial.print(lin_acc);
  Serial.print(" ");
  Serial.print(45);
  Serial.print(" ");
  Serial.println(3);
  */
  Serial.print(lin_acc);
  /*
  Serial.print(" ");
  Serial.print(gyro_vel);
  */
  
  Serial.print(" ");
  Serial.print(hrp[3] - hrp[0]);
  Serial.print(" ");
  Serial.print(hrp[4] - hrp[1]);
  Serial.print(" ");
  Serial.println(hrp[5] - hrp[2]);
  

  /*
  Serial.print(" ");
  Serial.print(hrp[3]);
  Serial.print(" ");
  Serial.print(hrp[4]);
  Serial.print(" ");
  Serial.println(hrp[5]);
  */
  
  if(lin_acc <= 3)
  {
    uhTime = millis();
  }
  
  unsigned long tTime = millis();
  if (lin_acc >= 35 && tTime - uhTime <= 50)
  {
    ohTime = millis();
    
    if(gyro_vel >= 300)
    {
      if(hrp[3]-hrp[0] >= 30 || hrp[3]-hrp[0] <= -30 || hrp[4]-hrp[1] >= 30 || hrp[4]-hrp[1] <= -30 || hrp[5]-hrp[2] >= 30 || hrp[5]-hrp[2] <= -30){
        //Serial.println("sensor gedreht");
        //Serial.println("ex");
        exit(0);
      }
    }

       
  }
}

float standard(float *hrp){
  float heading, roll, pitch;
  for(int i=0;i<=500;i){
    if(IMU.eulerAnglesAvailable())
        IMU.readEulerAngles(heading, roll, pitch);
        hrp[0] = hrp[0] + heading;
        hrp[1] = hrp[1] + roll;
        hrp[2] = hrp[2] + pitch;
        i++;    
  }
  hrp[0] = hrp[0]/500;
  hrp[1] = hrp[1]/500;
  hrp[2] = hrp[2]/500;
}
