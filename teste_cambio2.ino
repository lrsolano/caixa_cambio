#include <IRremote.h>  
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
// Inicializa o display no endereco 0x27
LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7,3, POSITIVE);

int RECV_PIN = 12;  
float armazenavalor;  
int LED1 = 2;  
int LED2 = 3;
int LED3 = 4;
int LED4 = 5; 
int LED5 = 6; 
int LED6 = 7; 
int LED7 = 8;
int coluna = 7;
int linha = 12;
char matriz[12][7];
  
IRrecv irrecv(RECV_PIN);  
decode_results results;  

#include <IRremote.h>  

void setup() {
  // put your setup code here, to run once:
  lcd.begin (16,2);
  lcd.clear();
  lcd.setCursor(0,0);  
  lcd.print("Sistema Cambio");
  lcd.setCursor(0,1);  
  lcd.print("Aguradando");
  pinMode(LED1, OUTPUT);   
  pinMode(LED2, OUTPUT); 
  pinMode(LED3, OUTPUT);  
  pinMode(LED4, OUTPUT); 
  pinMode(LED5, OUTPUT);
  pinMode(LED6, OUTPUT);
  pinMode(LED7, OUTPUT);   
  Serial.begin(9600);  
  irrecv.enableIRIn(); // Inicializa o receptor IR  
  //zerar matriz
  //primeira linha 1° marcha segunda linha 2°....
  for (int x = 0; x < linha; x++ ){
      for (int y = 0; y < coluna; y++){
        matriz[x][y] = 0;
      }
    }
}

//Função para ligar os leds
void ligar(int numero){
       int numero1 = numero - 1;
       Serial.println("Valores");
       for (int cursory = 0; cursory < 7; cursory++){
       Serial.println(matriz[numero1][cursory]);
       if (matriz[numero1][cursory]=='1'){
        digitalWrite(LED1,HIGH);
       }
       if (matriz[numero1][cursory]=='2'){
        digitalWrite(LED2,HIGH);
       }
       if (matriz[numero1][cursory]=='3'){
        digitalWrite(LED3,HIGH);
       }
       if (matriz[numero1][cursory]=='4'){
        digitalWrite(LED4,HIGH);
       }
       if (matriz[numero1][cursory]=='5'){
        digitalWrite(LED5,HIGH);
       }
       if (matriz[numero1][cursory]=='6'){
        digitalWrite(LED6,HIGH);
       }
       if (matriz[numero1][cursory]=='7'){
        digitalWrite(LED7,HIGH);
       }      
      }
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //verifica  se tem 52 numeros esperando para serem lidos, para não dar erro quando for salvar a matriz
  if(Serial.available()>41){              
    for (int x = 0; x < 12; x++ ){   
      for (int y = 0; y < 7; y++){
        lcd.setCursor(0,1); 
        lcd.print("Carregando                     ");
        //Realiza a leitura
        matriz[x][y] = Serial.read();
        delay(110);        
      }    
     }
  //Apga o restante dos dados não lidos caso tenha
  while (Serial.available()>0){
    char lixeira = Serial.read();
  }
  lcd.setCursor(0,1); 
  lcd.print("Carregado                     ");     
    } 
//Lê as informações recebidas do controle
if (irrecv.decode(&results)){  
    armazenavalor = (results.value); 
    if (armazenavalor == 1 or armazenavalor == 2049){
       lcd.setCursor(0,1);  
       lcd.print("Marcha 1               ");               
       ligar(1);  
    }  
    if (armazenavalor == 2 or armazenavalor == 2050){   
       lcd.setCursor(0,1);  
       lcd.print("Marcha 2               ");          
       ligar(2);    
    }  
    if (armazenavalor == 3 or armazenavalor == 2051){   
      lcd.setCursor(0,1);  
      lcd.print("Marcha 3                ");          
      ligar(3);    
    }  
    if (armazenavalor == 4 or armazenavalor == 2052){
      lcd.setCursor(0,1);  
      lcd.print("Marcha 4                ");             
      ligar(4);    
    }  
    if (armazenavalor == 5 or armazenavalor == 2053){
      lcd.setCursor(0,1);  
      lcd.print("Marcha 5                ");           
      ligar(5);    
    }  
    if (armazenavalor == 6 or armazenavalor == 2054){ 
      lcd.setCursor(0,1);  
      lcd.print("Marcha 6               ");          
      ligar(6);    
    }  
    if (armazenavalor == 7 or armazenavalor == 2055){  
      lcd.setCursor(0,1);  
      lcd.print("Marcha 7               ");         
      ligar(7);    
    }  
    if (armazenavalor == 8 or armazenavalor == 2056){  
      lcd.setCursor(0,1);  
      lcd.print("Marcha 8               ");         
      ligar(8);  
    } 
    if (armazenavalor == 9 or armazenavalor == 2057){  
      lcd.setCursor(0,1);  
      lcd.print("Marcha 9               ");         
      ligar(9);  
    } 
    if (armazenavalor == 0 or armazenavalor == 2048){ 
      lcd.setCursor(0,1);  
      lcd.print("Marcha 10               ");          
      ligar(10);  
    } 
    if (armazenavalor == 32 or armazenavalor == 2080){
      lcd.setCursor(0,1);  
      lcd.print("Marcha 11               ");           
      ligar(11);  
    } 
    if (armazenavalor == 41 or armazenavalor == 2089){ 
      lcd.setCursor(0,1);  
      lcd.print("Marcha 12               ");          
      ligar(12);  
    } 
     if (armazenavalor == 12 or armazenavalor == 2060){           
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, LOW);
      digitalWrite(LED4, LOW);
      digitalWrite(LED5, LOW);
      digitalWrite(LED6, LOW);
      digitalWrite(LED7, LOW);
      lcd.setCursor(0,1);  
      lcd.print("Sem marcha               ");     
    } 
    irrecv.resume();     
  } 
}
  
