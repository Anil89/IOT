#include <SimpleDHT.h>
SimpleDHT11 dht11;  //decaling one object of typr class SimpleDHT11 to//use the functions from that class
int sensorpin=A0;
void setup() {    Serial.begin(9600);   }
void loop() { byte temperature=0;
byte humidity=0;
dht11.read(sensorpin,&temperature, &humidity,NULL);
Serial.print(temperature);
Serial.print(",");
Serial.println(humidity);
delay(200);               }
