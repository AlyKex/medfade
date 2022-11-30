
#include <MKRIMU.h>





unsigned long mySTime;

String acccheck = "abc";

float x, y, z;

void setup() {



  
Serial.begin(2000000);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }

  

     delay(10000);
     Serial.println(acccheck);
     delay(1000);
     mySTime = millis();
}

void loop() {

  
    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(x, y, z);
      acccheck = "lb";
      printEvent(x, y, z);
    }
    
    if (IMU.accelerationLinAvailable()) {
      IMU.readLinAcceleration(x, y, z);
      acccheck = "lk";
      printEvent(x, y, z);  
    }
    
      if (IMU.eulerAnglesAvailable()) {
      IMU.readEulerAngles(x, y, z);
      acccheck = "ow";
      printEvent(x, y, z);
     }


  

  
  if(millis() - mySTime > 10000){
      acccheck = "et";

      Serial.print(acccheck);Serial.print(" ");
      Serial.println(millis() - mySTime);
      exit(0);
  }
}

void printEvent(float x, float y, float z) {

  Serial.print(acccheck);Serial.print(" ");
  Serial.print(x, 2); Serial.print(" ");
  Serial.print(y, 2); Serial.print(" ");
  Serial.println(z, 2);
}
