const int LED_YELLOW = 8;
const int LED_WHITE = 2;
const int LED_RED = 13;
const int LED_GREEN = 12;
const int GROUND_PIN6 = 6;
const int PULSADOR7 = 7;

void setup() {
  Serial.begin(9600);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_WHITE, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(PULSADOR7, INPUT);

}


void loop() {
  //Serial.println( digitalRead(PULSADOR7) == HIGH ? '1' : '0');
  switch(Serial.read())
  {
    // LED YELLOW.
    case '9':
      digitalWrite(LED_YELLOW, HIGH);
      //delay(1000);
      break;
    case '8':
      digitalWrite(LED_YELLOW, LOW);
      //delay(1000);
      break;
    // LED RED.
    case '7':
      digitalWrite(LED_RED, HIGH);
      //delay(1000);
      break;
    case '6':
      digitalWrite(LED_RED, LOW);
      //delay(1000);
      break;
    // LED WHITE.
     case '5':
      digitalWrite(LED_WHITE, HIGH);
      //delay(1000);
      break;
     case '4':
      digitalWrite(LED_WHITE, LOW);
      //delay(1000);
      break;
     case '3':
      digitalWrite(LED_GREEN, HIGH);
      //delay(1000);
      break;
     case '2':
      digitalWrite(LED_GREEN, LOW);
      //delay(1000);
      break;
     case '1':
      digitalWrite(LED_YELLOW, HIGH);
      digitalWrite(LED_RED, HIGH);
      digitalWrite(LED_WHITE, HIGH);
      break;
     case '0':
      digitalWrite(LED_YELLOW, LOW);
      digitalWrite(LED_GREEN, LOW);
      digitalWrite(LED_RED, LOW);
      digitalWrite(LED_WHITE, LOW);
      break;
     
  }
}
  
  
/*
 * RUTINA UTILIZADA PARA EXAMEN
void loop()
{
  switch(Serial.read())
  {
    // LED YELLOW.
    case '2':
    {
      digitalWrite(LED_RED, LOW);
      digitalWrite(LED_YELLOW, LOW);
      digitalWrite(LED_WHITE, LOW);
      break;
    }
    case '1':
      digitalWrite(LED_RED, LOW);
      digitalWrite(LED_YELLOW, HIGH);
      digitalWrite(LED_WHITE, HIGH);
      delay(1000);
      break;
    case '0':
      digitalWrite(LED_RED, HIGH);
      digitalWrite(LED_YELLOW, HIGH);
      digitalWrite(LED_WHITE, LOW);
      delay(1000);
      break;
  }
}*/
