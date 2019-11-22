#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
uint8_t servonum = 0;
#define SERVO_FREQ 60

#define VALUE_MAIL 80
#define VALUE_NOMAIL 500

bool email = false;
int value = VALUE_NOMAIL;

void setup() {
  Serial.begin(9600);
  
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);

}

void loop() {
  if (Serial.available()) {
    String command = Serial.readString();
    if (command == "mail") {
      value = VALUE_MAIL;
    }

    if (command == "nomail") {
      value = VALUE_NOMAIL;
    }

    Serial.println(command);
  }

  pwm.setPWM(servonum, 0, value);

  //Serial.println(value);
}
