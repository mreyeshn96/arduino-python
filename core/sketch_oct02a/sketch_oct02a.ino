/*
 * RUTINA: DOS LED PULSADOR.
 * DESCRIPCION: ESTA RUTINA CAMBIARA DE LED MIENTRAS ESTE PRESIONADO.
 */

/*
const int LED13 = 13;
const int LED2 = 2;
const int PULSADOR = 7;

void setup() {
  Serial.begin(9600);
  pinMode(PULSADOR, INPUT);
  pinMode(LED13, OUTPUT);
  pinMode(LED2, OUTPUT);

  digitalWrite(LED13, LOW);
  digitalWrite(LED2, LOW);
}

void loop() {
  if( digitalRead(PULSADOR)== LOW )
  {
    digitalWrite(LED13, HIGH);
    digitalWrite(LED2, LOW);
  }
  else
  {
    digitalWrite(LED13, LOW);
    digitalWrite(LED2, HIGH);
  }
  
}
*/

/*
 * RUTINA: UN LED PULSADOR
 * DESCRIPCION: ESTA RUTINA APAGARA O ENCENDERA UN LED INDICADO BASADO EN EL PULSADOR.
 */

const int LED13 = 13;
const int LED2 = 2;
const int PULSADOR = 7;
bool estadoPulsador = false;

void setup(){
  Serial.begin(9600);
  pinMode(PULSADOR, INPUT);
  pinMode(LED13, OUTPUT);
  pinMode(LED2, OUTPUT);

  digitalWrite(LED13, HIGH);
  digitalWrite(LED2, LOW);
  digitalWrite(PULSADOR, LOW);
}

void loop() {
  
    //estadoPulsador = 
    if( digitalRead(PULSADOR) )
    {
      Serial.println("1");
      digitalWrite(LED13,  !digitalRead(LED13));
      digitalWrite(LED2,  !digitalRead(LED2));
      delay(1000);

      if( digitalRead(PULSADOR) )
      {
        Serial.println("1");
      }
      else
      {
        Serial.println("0");
      }
    }
    else
    {
      
    }
  }


/**********/
/*
const int LED13 = 13;
const int LED2 = 2;
const int PULSADOR = 7;
//bool estadoPulsador = false;
bool estadoLEDS = false;

void setup(){
  Serial.begin(9600);
  pinMode(PULSADOR, INPUT);
  pinMode(LED13, OUTPUT);
  pinMode(LED2, OUTPUT);

  digitalWrite(LED13, HIGH);
  digitalWrite(LED2, LOW);
}

void loop() {
  if( digitalRead(PULSADOR) == HIGH )
    {

      if( estadoLEDS = true )
      {
        digitalWrite(LED13,  !digitalRead(LED13));
        digitalWrite(LED2,  !digitalRead(LED2));
        Serial.println("1");
        estadoLEDS = !estadoLEDS;  
      }
      else
      {
        Serial.println("0");
        estadoLEDS = !estadoLEDS;  
      }
      
      delay(1000);
    }
    else
    {
      
//      delay(1000);
    }
}
*/



/*
 * RUTINA: ENCENDER O APAGAR LED INDIVIDUALMENTE.
 * DESCRIPCION: ESTA RUTINA ENCENDERA Y APAGAR UN LED EN ESPECIFICO DESDE UNA INTERFAZ PYTHON.
 */

/*const int LED1 = 13;
const int LED2 = 2;
const int PULSADOR = 7;
bool estadoLED1 = false;
bool estadoLED2 = false;

void setup(){
  Serial.begin(9600);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  estadoLED1 = false;
  estadoLED2 = false;
}

void loop() {
  if(Serial.available())
  {
    char c = Serial.read();
    if( c == '9' )
    {
      digitalWrite(LED1, HIGH);
      delay(1000);
    }
    else if(c == '8' )
    {
       digitalWrite(LED1, LOW);
       delay(1000);
    }
    
    if( c == '5' )
    {
      digitalWrite(LED2, HIGH);
      delay(1000);
    }
    else if( c == '4' )
    {
      digitalWrite(LED2, LOW);
      delay(1000);
    }
  }
}*/

/*const int LED = 13;
const int BOTON = 7;
int va1 = 0;
int state = 0;
int old_va1 = 0;
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(BOTON, INPUT);
}

void loop() {
  va1 = digitalRead(BOTON);
  if( (va1 == HIGH) && (old_va1 == LOW) ) {
    state=1-state;
    // Serial.println("on");
    // delay(100); 
  }
  old_va1 = 1;
  if( state==1 ) {
    digitalWrite(LED, HIGH);
    Serial.println("1");
    delay(1);
  }
  else {
    digitalWrite(LED, LOW);
    Serial.println("0");
  }
  delay(200);
}*/

/*int led = 13;
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  // put your setup code here, to run once:

}*/


/*void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(2, OUTPUT);
  //pinMode(BOTON, INPUT);
}


void loop() {
  if(Serial.available())
  {
    char c=Serial.read();
    if(c=='9')
    {
      digitalWrite(13, HIGH);
      delay(1000);
    }
    if(c=='5')
    {
      digitalWrite(2, HIGH);
      delay(1000);
    }
    if(c=='4')
    {
      digitalWrite(2, LOW);
      delay(1000);
    }
    if(c=='8')
    {
      digitalWrite(13, LOW);
      delay(1000);
    }
    if(c=='0')
    {
      digitalWrite(13, LOW);
      digitalWrite(2, LOW);
      delay(1000);
    }
  }
}*/
