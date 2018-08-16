#include <SimpleDHT.h>
SimpleDHT11 dht11;
int senspin=A1;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
byte temp=0;
byte hum=0;
dht11.read(senspin,&temp,&hum,NULL);
Serial.println(temp);
delay(5000);
}
