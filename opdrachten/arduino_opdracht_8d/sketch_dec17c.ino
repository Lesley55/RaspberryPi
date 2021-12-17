const int gpioPins26 = 26;
const int gpioPins19 = 19;
const int KNOP_PIN = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(gpioPins26, OUTPUT);
  pinMode(gpioPins19, OUTPUT); 
  pinMode(KNOP_PIN, INPUT);
  
}
void loop() {
  if(digitalRead(KNOP_PIN) == HIGH){
      digitalWrite(gpioPins26, HIGH);
      digitalWrite(gpioPins19, LOW);
  } else {
      digitalWrite(gpioPins26, LOW);
      digitalWrite(gpioPins19, HIGH);
  }
}
