#include <MKRIMU.h>



double acc_data_compare;

long lhTime;
String acccheck = "abc";

float x, y, z;

void setup() {


  
Serial.begin(2000000);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }

  

     delay(5000);
     Serial.println(acccheck);
     delay(1000);
}

void loop() {


    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(x, y, z);
      acccheck = "lb";
      //printEvent(x, y, z);
      acc_data_compare = (abs(x) + abs(y) + abs(z));

      compare(acc_data_compare, lhTime);

    

    }



/*
      if (IMU.eulerAnglesAvailable()) {
      IMU.readEulerAngles(x, y, z);
      acccheck = "ow";
      printEvent(x, y, z);
     }
*/
     

     


/*    
  if(millis() - mySTime > 2000000000){
      

      Serial.print(acccheck);Serial.print(" ");
      Serial.println(millis() - mySTime);
      exit(0);
  }
*/
}

void printEvent(float x, float y, float z) {

  Serial.print(acccheck);Serial.print(" ");
  Serial.print(x, 2); Serial.print(" ");
  Serial.print(y, 2); Serial.print(" ");
  Serial.println(z, 2);
}

void compare(double acc_data,long &lhTime){
  unsigned long tTime;
   //Ausgabe von Überprüfwerten
  Serial.print("normal:");
  Serial.print(" ");
  Serial.print(acc_data);
  Serial.print(" ");
  Serial.print(45);
  Serial.print(" ");
  Serial.println(2.7);
  
  
  
  if(acc_data <= 2.7){
    Serial.println(" untereracc threshhold erreicht");
    lhTime = millis();
  }
  
  tTime = millis();
  if (acc_data >= 45 && tTime - lhTime <= 500){
    Serial.println("oberer threshold erreicht");
  }
}
