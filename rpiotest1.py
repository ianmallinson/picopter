from RPIO import PWM

servo = PWM.Servo()
pulse = 1000
while (True):
  pulse = input("Pulse width (ns):")
  for chan in [5,6,12,13]:  
    servo.set_servo(chan, pulse)

  



