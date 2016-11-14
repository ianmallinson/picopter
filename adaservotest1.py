import sys
sys.path.append('/home/pi/picopter/Adafruit/Adafruit_PWM_Servo_Driver/')
from  Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(244)
pulse = 1000
while (True):
  pulse = input("Pulse width (ns):")
  for chan in range(4):  
    pwm.setPWM(chan, 0, pulse)

  



