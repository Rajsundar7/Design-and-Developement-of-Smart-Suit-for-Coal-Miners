
#include <LoRa.h>



void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Receiver Host");
 
  if (!LoRa.begin(433E6)) {
    Serial.println("LoRa Error");
    while (1);
  }
}
void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    Serial.print("Receiving Data: ");
    while (LoRa.available()) {
      String data = LoRa.readString();
      Serial.println(data);
      
    }
  }
  delay(200);
}
