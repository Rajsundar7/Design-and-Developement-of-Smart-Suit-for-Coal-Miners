#include <Wire.h>
#include <SFE_BMP180.h>
#include <LoRa.h>



//#define SS 15
//#define RST 16
//#define DIO0 2

String data = "Iconic";


SFE_BMP180 bmp180;

int mq2 = 0;
int mq9 = 0;



void setup() {  
  
  Serial.begin(115200);
  Serial.println("TEAM ICONIC ZIPPY'S");
  bool success = bmp180.begin();


  if (success) {
    
    Serial.println("System Started ");
  }
  else
  {
    Serial.println("Bmp Error");
  }


  
  while (!Serial);
  Serial.println("Sender Host");
  
  if (!LoRa.begin(433E6)) {
    Serial.println("LoRa Error");
    delay(100);
    while (1);
  }

  /*while (!Serial);
  Serial.println("Sender Host");
  LoRa.setPins(SS, RST, DIO0);
  if (!LoRa.begin(433E6)) {
    Serial.println("LoRa Error");
    delay(100);
    while (1);
  }*/
}

void loop() 
{

    char status;
    double T, P;
    bool success = false;

    mq2 = analogRead(A0);
    mq9 = analogRead(A1);


    status = bmp180.startTemperature();
    
    if (status != 0) 
    {
      delay(status);
      status = bmp180.getTemperature(T);
    

      if (status != 0) 
      {
        status = bmp180.startPressure(3);
         if (status != 0)
         {
            delay(status);
            status = bmp180.getPressure(P, T);
            delay(200);
            if (status != 0) 
            {
               Serial.print("Pressure: ");
               Serial.print(P);
               Serial.println(" hPa");
      
               Serial.print("Temperature: ");
               Serial.print(T);
               Serial.println(" C"); 

               delay(200);
              
              }
             }
        
             
            }
           }


              Serial.print("Sending Data: ");

              Serial.println("mq9 =");
              Serial.println(mq9);
              
              Serial.println("mq2 = ");
              Serial.println(mq2);
               delay(200);
               data += mq2;
               data += " ";

               data += mq9;
               data += " ";

               data += P;
               data += " ";

               data += T;
               data += " ";

              
              Serial.println(data);
              LoRa.beginPacket();
              LoRa.print(data);
              LoRa.endPacket();
              data = "";
              delay(2000);
              


           
}
