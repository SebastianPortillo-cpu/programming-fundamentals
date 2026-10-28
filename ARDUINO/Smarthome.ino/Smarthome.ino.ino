const int light_kitchen = 10;
const int light_bathroom = 11;
const int light_bedroom = 12;
const int light_livingroom = 13;
char opt;
void setup() {

  //

  pinMode(light_kitchen,OUTPUT);
  pinMode(light_bathroom,OUTPUT);
  pinMode(light_bedroom,OUTPUT);
  pinMode(light_livingroom,OUTPUT);

  //Permite decirle a lo que este conectado al pin apagar o encender 

  digitalWrite(light_kitchen,LOW);
  digitalWrite(light_bathroom,LOW);
  digitalWrite(light_bedroom,LOW);
  digitalWrite(light_livingroom,LOW);

  //Serail.begin es para poder comunicarnos con la placa de arduino y Serail.print es para mostrar el mensaje en pantalla

  Serial.begin(9600); //Baud
  Serial.println("¡Welcome to my SmartHome!");
  mainMenu();

}

//empaquetar codigo para 

void mainMenu() {

  Serial.println(":::MAIN MENU:::");
  Serial.println("[1]. Turn on light kitchen");
  Serial.println("[2]. Turn off light kitchen");
  Serial.println("[3]. Turn on light bathroom");
  Serial.println("[4]. Turn off light bathroom");
  Serial.println("[5]. Turn on light bedroom");
  Serial.println("[6]. Turn off light bedroom");
  Serial.println("[7]. Turn on light livingroom");
  Serial.println("[8]. Turn off light livingroom");
  Serial.println("[9]. Turn on all");
  Serial.println("[10]. Turn off all");


}


void loop() {

  
  if(Serial.available()>0){
     
     opt=Serial.read();
     if(opt=='1'){
      digitalWrite(light_kitchen,HIGH);
     }
     if(opt=='2'){
      digitalWrite(light_kitchen,LOW);
     }
  }

}
