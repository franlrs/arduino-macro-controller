// Arduino pin numbers
const int SW_pin = 2; // digital pin connected to switch output
const int X_pin = A0; // analog pin connected to X output
const int Y_pin = A1; // analog pin connected to Y output

void setup() {
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(X_pin));
  Serial.print(",");  // Separator
  Serial.print(analogRead(Y_pin));
  Serial.print(",");  // Separator
  Serial.println(digitalRead(SW_pin)); 
  
  delay(250); 
  // A shorter delay makes the joystick respond faster
  // Increase this value if you need more stability
}