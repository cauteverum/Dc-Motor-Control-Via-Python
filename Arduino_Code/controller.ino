int in1 = 8; 
int in2 = 9; 
int enA = 7; 
byte data; 
int flag = 0; 

void setup() {
  pinMode(in1, OUTPUT); 
  pinMode(in2, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available()){
     data = Serial.parseInt(); 
      if (data == 1 && flag == 0){
        digitalWrite(enA, HIGH); 
        flag = 1; 
      }
      if (data == 2 && flag == 1){
        digitalWrite(enA, LOW); 
        flag = 0; 
      }
      if (data == 3){
        digitalWrite(in1, HIGH); 
        digitalWrite(in2, LOW); 
        }
      
      if (data == 4){
        digitalWrite(in1, LOW); 
        digitalWrite(in2, HIGH); 
      }
      if (data > 4 && flag == 1){
        digitalWrite(enA, data);  
      }
    }
}
