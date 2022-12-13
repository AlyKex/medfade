#include <MKRIMU.h>

unsigned long mySTime;

double acc_data_compare[6];
double acc_lin_data_compare[6];


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
     mySTime = millis();
}

void loop() {


    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(x, y, z);
      acccheck = "lb";
      //printEvent(x, y, z);
      acc_data_compare[5] = (abs(x) + abs(y) + abs(z));

      compare(acc_data_compare);

     for(int i=0;i<=4;i++){
        acc_data_compare[i] = acc_data_compare[i+1];
      }

     acc_data_compare[5] = 0;
    

    }

/*
    if (IMU.accelerationLinAvailable()) {
      IMU.readLinAcceleration(x, y, z);
      acccheck = "lk";
      printEvent(x, y, z);  
      acc_lin_data_compare[4] = x + y + z;

      compare(acc_lin_data_compare);

     for(int i=0;i<=3;i++){
        acc_lin_data_compare[i] = acc_lin_data_compare[i+1];
      }
    }
*/


      if (IMU.eulerAnglesAvailable()) {
      IMU.readEulerAngles(x, y, z);
      acccheck = "ow";
      printEvent(x, y, z);
     }

     

     


  
  if(millis() - mySTime > 2000000000){
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

void compare(double acc_array[6]){
  /* //Ausgabe von Überprüfwerten
  Serial.print("normal:");
  Serial.print(" ");
  Serial.print(acc_array[5]);
  Serial.print(" ");
  Serial.println(acc_array[5] - acc_array[0]);
  */
  if(acc_array[5] - acc_array[0] >= 50){
    Serial.println("acc threshhold erreicht");
    
    for(int i=0;i<=5;i++){
        Serial.println(acc_array[i]);
      }
    Serial.println("----------");
    Serial.println(acc_array[5] - acc_array[0]);
    Serial.println("----------");

    exit(0);
    
  }
}
