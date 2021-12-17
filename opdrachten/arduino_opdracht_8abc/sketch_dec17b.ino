const int led8 = 8;
const int led9 = 9;
const int rasberry12 = 12; 
const int rasberry13 = 13;
const int knop = 7;
const int rasberry5 = 5;
void setup() {
  // put your setup code here, to run once:
  pinMode(led8, OUTPUT);
  pinMode(led9, OUTPUT);
  pinMode(rasberry12, INPUT);
  pinMode(rasberry13, INPUT);
  pinMode(knop, INPUT);
  pinMode(rasberry5, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(rasberry12) == HIGH){
      digitalWrite(led8, HIGH);
  } else {
      digitalWrite(led8, LOW);
  }
  if(digitalRead(rasberry13) == HIGH){
      digitalWrite(led9, HIGH);
  } else {
      digitalWrite(led9, LOW);
  }
  if(digitalRead(knop) == HIGH){
      digitalWrite(rasberry5, HIGH);
  } else {
      digitalWrite(rasberry5, LOW);
  }
}
