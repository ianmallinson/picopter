from RPIO import PWM

servo = PWM.Servo()
demand = 0
while (True):
  chan = input("Channel:")
  width = input ("Width:")  
  servo.set_servo(chan, width)

    

  



