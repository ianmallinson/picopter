# import packages
from RPIO import PWM
import pygame
from pygame.locals import *

#initialise classes
servo = PWM.Servo(0,20000,10)
pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Key Press Test")
f1=pygame.font.SysFont("comicsansms",24)

#define functions
def setspeed(demand):
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

def setsteer(demand): 
  servo.set_servo(13, (1500+(demand*50))) 

speeddemand=0
steerdemand=0

#main loop
while (True):
  for i in pygame.event.get():
    press=pygame.key.get_pressed()
    for i in xrange(0,len(press)):
      if press[i]==1:
        name=pygame.key.name(i)
        if name=="left":
          steerdemand -=3
          setsteer(steerdemand)
        elif name=="right":
          steerdemand +=3
          setsteer(steerdemand)
        elif name=="up":
          speeddemand +=1
          setspeed(speeddemand)
        elif name=="down":
          speeddemand -=1
          setspeed(speeddemand)
        screen.fill((255,255,255))
        text=f1.render(name,True,(0,0,0))
        screen.blit(text,(100,100))
        text2=f1.render("Steering %s" % str(steerdemand),True,(0,0,0))
        screen.blit(text2,(100,150))
        text3=f1.render("Speed %s" % str(speeddemand),True,(0,0,0))
        screen.blit(text3,(100,200))
#    text4=f1.render("Heading %s" % str(int(math.degrees(fusionPose[2]))),True,(0,0,0))
#    screen.blit(text4,(100,250))
        pygame.display.update()



