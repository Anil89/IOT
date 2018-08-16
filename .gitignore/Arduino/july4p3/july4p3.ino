int sensorpin=A2;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);}
void loop() {
  // put your main code hsensorpinere, to run repeatedly:
int proximity=analogRead(sensorpin);
Serial.println(proximity);
delay(200);;
}
