int x;
int in1 = 8; 
int in2 = 9; 
int enable = 11; 
int run_ = 0; 

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 pinMode(in1, OUTPUT); 
 pinMode(in2, OUTPUT);
 pinMode(enable, OUTPUT);
}


void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 if (x == -1){run_ = 1;}
 else if (x == -2){
  Serial.print("Durduruluyor."); 
  digitalWrite(in1, LOW); 
  digitalWrite(in2, LOW); 
  digitalWrite(enable, LOW); 
  run_ = 0; 
 }
 else if (x == -3 && run_) {
  digitalWrite(in1, HIGH); 
  digitalWrite(in2, LOW); 
  Serial.print("in1 aktif"); 
 }
 else if (x == -4 && run_) {
  digitalWrite(in1, LOW); 
  digitalWrite(in2, HIGH); 
  Serial.print("in2 aktif"); 
 }
 if (x < 5 && x > 0){
  analogWrite(enable, LOW); 
  Serial.print("enable cikisi 0");
 }
 else if (x > 5 && run_) {
  analogWrite(enable, x); 
  Serial.print("Pwm aktif "); 
  Serial.print(x); 
 }
 
}
