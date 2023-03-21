#include "Adafruit_FONA.h"
#include "Secrets.h"
#include "BNO055.h"

void FonaStartUp(Adafruit_FONA fona) {

  char replybuffer[255];
  uint8_t readline(char *buff, uint8_t maxbuff, uint16_t timeout = 0);

  uint8_t type;

  type = fona.type();
  Serial.println(F("-----------------------------------------"));

  Serial.println(F("FONA is OK"));
  Serial.println(F("-----------------------------------------"));

  char imei[16] = { 0 };
  uint8_t imeiLen = fona.getIMEI(imei);
  if (imeiLen > 0) {
    Serial.print("Module IMEI: ");
    Serial.println(imei);
  }
  Serial.println(F("-----------------------------------------"));

  //GET CCID
  fona.getSIMCCID(replybuffer);
  Serial.print(F("SIM CCID = "));
  Serial.println(replybuffer);
  Serial.println(F("-----------------------------------------"));


  //GET RSSI
  uint8_t n = fona.getRSSI();
  int8_t r;

  Serial.print(F("RSSI = "));
  Serial.print(n);
  Serial.print(": ");
  if (n == 0) r = -115;
  if (n == 1) r = -111;
  if (n == 31) r = -52;
  if ((n >= 2) && (n <= 30)) {
    r = map(n, 2, 30, -110, -54);
  }
  Serial.print(r);
  Serial.println(F(" dBm"));
  Serial.println(F("-----------------------------------------"));

  //GET Network/Cellular State
  uint8_t net = fona.getNetworkStatus();
  Serial.println(F("Network registration"));
  while (fona.getNetworkStatus() != 1) {
    Serial.println(".");
  }
  Serial.print(F("Network status "));
  Serial.print(net);
  Serial.print(F(": "));
  if (net == 1) Serial.println(F("Registered (home)"));
  Serial.println(F("-----------------------------------------"));


  //ACTIVATE GPS
  if (!fona.enableGPS(true)) {
    Serial.println(F("Failed to turn on"));
  } else {
    Serial.println(F("GPS Activated"));
  }
  Serial.println(F("-----------------------------------------"));



  //ACTIVATE GPRS
  while (!fona.enableGPRS(true)) {
    Serial.println(F("Failed to turn on"));
    fona.enableGPRS(false);
    delay(100);
  }
  Serial.println(F("GPRS Activated"));

  Serial.println(F("-----------------------------------------"));

  fona.setHTTPSRedirect(true);
}

//Send FallEvent
void SendFall(Adafruit_FONA fona){
  Serial.println(F("Sending JSON Object to server"));

  uint16_t statuscode;
  int16_t length;
  char url[] = SECRET_URL;
  char data[] = "{\"fallState\": true}";

  Serial.println(F("NOTE: in beta! Use simple websites to post!"));
  Serial.print(F("Sending request to URL: "));
  Serial.println(url);
  Serial.print(F("Request data: "));
  Serial.println(data);

  while (!fona.HTTP_POST_start(url, F("application/json"), (uint8_t *)data, strlen(data), &statuscode, (uint16_t *)&length)) {
    Serial.println(F("Failed to start HTTP POST request!"));
  }

  Serial.println(F("HTTP POST request started successfully."));

  int i = 0;
  char c;
  while (length > 0) {
    while (fona.available()) {
      c = fona.read();

#if defined(__AVR_ATmega328P__) || defined(__AVR_ATmega168__)
      loop_until_bit_is_set(UCSR0A, UDRE0); /* Wait until data register empty. */
      UDR0 = c;
#else
      Serial.write(c);
#endif
      length--;
      i++;
      if (i > strlen(data) || length == 0) break;
    }
  }

  Serial.println(F("\n****"));
  Serial.println(F("HTTP POST request completed."));
  Serial.print(F("Response status code: "));
  Serial.println(statuscode);

  fona.HTTP_POST_end();
}

void SendGPS(){

}


void flushSerial() {
  while (Serial.available())
    Serial.read();
}

char readBlocking() {
  while (!Serial.available())
    ;
  return Serial.read();
}
uint16_t readnumber() {
  uint16_t x = 0;
  char c;
  while (!isdigit(c = readBlocking())) {
    //Serial.print(c);
  }
  Serial.print(c);
  x = c - '0';
  while (isdigit(c = readBlocking())) {
    Serial.print(c);
    x *= 10;
    x += c - '0';
  }
  return x;
}

uint8_t readline(char *buff, uint8_t maxbuff, uint16_t timeout) {
  uint16_t buffidx = 0;
  boolean timeoutvalid = true;
  if (timeout == 0) timeoutvalid = false;

  while (true) {
    if (buffidx > maxbuff) {
      //Serial.println(F("SPACE"));
      break;
    }

    while (Serial.available()) {
      char c = Serial.read();

      //Serial.print(c, HEX); Serial.print("#"); Serial.println(c);

      if (c == '\r') continue;
      if (c == 0xA) {
        if (buffidx == 0)  // the first 0x0A is ignored
          continue;

        timeout = 0;  // the second 0x0A is the end of the line
        timeoutvalid = true;
        break;
      }
      buff[buffidx] = c;
      buffidx++;
    }

    if (timeoutvalid && timeout == 0) {
      //Serial.println(F("TIMEOUT"));
      break;
    }
    delay(1);
  }
  buff[buffidx] = 0;  // null term
  return buffidx;
}

void StartLoop(Adafruit_FONA fona) {
  Serial.print(F("FONA> "));
  while (!Serial.available()) {
    if (fona.available()) {
      Serial.write(fona.read());
    }
  }
}
void EndLoop(Adafruit_FONA fona) {
  flushSerial();
  while (fona.available()) {
    Serial.write(fona.read());
  }
}
