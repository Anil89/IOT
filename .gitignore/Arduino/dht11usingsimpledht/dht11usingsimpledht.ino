#include <SimpleDHT.h>
SimpleDHT11 dht11;
int sensorpin = A2;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
byte temperature=0;
byte humidity=0;
dht11.read(sensorpin,&temperature,&humidity,NULL);
Serial.print(temperature);
Serial.print("  ");
Serial.println(humidity);
delay(100);}
