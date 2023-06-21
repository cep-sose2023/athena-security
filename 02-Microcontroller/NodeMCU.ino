//pins on the NodeMCU for the led and fan
int ledPin = 4;
int fanPin = 5;

String incoming; //string holds the incoming serial commands "on"/"off"
int sensorValue = 0;  //variable to store the value coming from the sensor

void setup() {
  delay(1000);
  //configure led and fan as output and turn them off by default
  pinMode(fanPin, OUTPUT);
  digitalWrite(fanPin, LOW);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);  //start the serial communication with 9600 baudrate
  delay(1000);
}

void loop() {
  
  static bool active = false; //stores the state of fan and led

  if (Serial.available() > 0) { //As soon as something is received via the serial interface
    incoming = Serial.readString();
    if (incoming == "on") { //activate fan and led when "on" is received
      digitalWrite(fanPin, HIGH);
      digitalWrite(ledPin, HIGH);
      delay(2000);
      active = true;
    } else if (incoming == "off") { //deactivate fan and led when "off" is received
      digitalWrite(fanPin, LOW);
      digitalWrite(ledPin, LOW);                      
      active = false;
    }
  }


  if (active) { //only run the code, when led and fan are on
    
    byte data = 0; //byte which is filled with random bits and later send to the API

    //the loop variable is used later to check if one Byte is filled with Bits before sending it
    for (int i = 0; i < 50; i++) {
      
     for (int a = 0; a < 4; a++) { //read the solar voltage 4 times with an interval of 5ms 
      int reading = analogRead(A0); //convert the solar voltage to int number (0V=0 |3.3V =1023)
      sensorValue = sensorValue + reading; //add the last reading to sensorValue
      delay(8); //wait 8ms (4 x 8ms = 32ms for full sensorValue)
    }

      byte lsb = (sensorValue & 0b11); //extract two LSBs from sensorValue
      sensorValue = 0; //clear sensorValue
      data = (data << 2) | lsb; //Add the two last extracted LSBs to data (Byte)
  
      if (i % 4 == 3) { //check if data (Byte) is filled with 8 LSBs
        Serial.write(data); //send the byte via the serial interface
        data = 0; //reset the byte after it has been sent
      }
    }
  }
}
