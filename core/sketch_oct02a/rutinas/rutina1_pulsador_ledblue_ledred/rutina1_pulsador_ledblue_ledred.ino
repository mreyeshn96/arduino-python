const int LED_RED = 13;
const int LED_BLUE = 2;
const int PULSADOR7 = 7;

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(PULSADOR7, INPUT);

  digitalWrite(LED_RED, HIGH);
}

void loop() {
  
  // Si se presiona el pulsador.
  
  if( digitalRead(PULSADOR7) )
  {
    Serial.println("1");
    digitalWrite(LED_RED, !digitalRead(LED_RED));
    digitalWrite(LED_BLUE, !digitalRead(LED_BLUE));
    delay(1000);
  }
  else if( digitalRead(PULSADOR7) == LOW )
  {
    Serial.println("0");
  } 
}
