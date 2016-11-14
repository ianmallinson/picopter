from RPIO import PWM

servo = PWM.Servo()
while (True):
  demand = input("Speed +/-10:")  
  if demand > 0:
    servo.set_servo(21, 0)
    servo.stop_servo(21)
    servo.set_servo(26, demand*2000)
  elif demand < 0:
    servo.set_servo(26, 0)
    servo.stop_servo(26)
    servo.set_servo(21, -demand*2000)
  else:
    servo.set_servo(21, 0)
    servo.set_servo(26, 0)
    servo.stop_servo(21)
    servo.stop_servo(26)

    

  



