
//Starker 11/07/2018

#define m11 2
#define m12 3
#define m21 4
#define m22 5
static int strdel=1000;
static int turdel=2000;
String shtstr="sllsssb";
int i=0;
//m11 & m12 for left pair ;m21 & m22 for right pair 

void setup()
{
pinMode(m11,OUTPUT);
pinMode(m12,OUTPUT);
pinMode(m21,OUTPUT);
pinMode(m22,OUTPUT);
Serial.begin(9600);
}

void loop()
{
  delay(3000);
/*

//Calibration space:
//straight:
straight();
delay(strdel);
stopper();
delay(3000);
straight();
delay(strdel);
stopper();
delay(3000);
left();
delay(turdel);
stopper();
delay(3000);
straight();
delay(turdel);
stopper();
delay(3000);

*/


//upon string reception:
Serial.print("start");
stopper();

for(i=0;shtstr[i]!='\0';i++){
if(shtstr[i]=='s')
{
straight();
delay(strdel);
Serial.print("s");
}

else if(shtstr[i]=='l')
{
left();
delay(turdel);
Serial.print("l");
}

else if(shtstr[i]=='r')
{
right();
delay(turdel);
Serial.print("r");
}

else if(shtstr[i]=='b')
{
reverse();
delay(strdel);
Serial.print("b");
}

else
{
stopper();
Serial.print("stop");
}
}

  Serial.println("out");
  
delay(7000);
}

void straight()
{

digitalWrite(m11,HIGH);
digitalWrite(m12,LOW);
digitalWrite(m21,HIGH);
digitalWrite(m22,LOW);

}

void left()
{

digitalWrite(m11,LOW);
digitalWrite(m12,HIGH);
digitalWrite(m21,HIGH);
digitalWrite(m22,LOW);

}

void right()
{

digitalWrite(m11,HIGH);
digitalWrite(m12,LOW);
digitalWrite(m21,LOW);
digitalWrite(m22,HIGH);

}

void reverse()
{

digitalWrite(m11,LOW);
digitalWrite(m12,HIGH);
digitalWrite(m21,LOW);
digitalWrite(m22,HIGH);

}

void stopper()
{

digitalWrite(m11,LOW);
digitalWrite(m12,LOW);
digitalWrite(m21,LOW);
digitalWrite(m22,LOW);

}


