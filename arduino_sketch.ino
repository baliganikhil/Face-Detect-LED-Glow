int incoming = 0;

void setup() {
   Serial.begin(9600);
   pinMode(13, OUTPUT);
}

void loop() {
   incoming = Serial.read();
   if (incoming != -1) {
      digitalWrite(13, LOW);
      Serial.println(incoming);
   } else {
      digitalWrite(13, HIGH);
   }

   Serial.flush();
}
