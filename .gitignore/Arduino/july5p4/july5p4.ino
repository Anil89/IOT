int sensorpin=A2;
//for digital
//int sensorpin=5;
void setup() {
Serial.begin(9600);
//pinMode(sensorpin,INPUT)          }
void loop() {
int gas=analogRead(sensorpin);
//int gas=digitalRead(sensorpin);
Serial.println(gas);
delay(100);}
