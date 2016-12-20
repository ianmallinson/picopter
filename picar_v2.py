# import packages
import sys
sys.path.append('/home/pi/picopter/Adafruit/Adafruit_PWM_Servo_Driver/')
from  Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO
import pygame
import mysocket


#initialise classes
pwm = PWM(0x40)
pwm.setPWMFreq(50)

GPIO.setmode(GPIO.BCM) #use GPIO numering
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) #set both motor channels to LOW
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)


#connect socket
comsocket = mysocket.mysocket()
comsocket.myhost('192.168.137.137',10000)


BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
size = [400,200]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pimobile remote window")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#define functions
def setspeed(spdemand):
    if spdemand > 50:
        GPIO.output(20, False)
        GPIO.output(21, True)
    elif spdemand < 50:
        GPIO.output(21, False)
        GPIO.output(20, True)
    pwm.setPWM(1,0,80*abs(spdemand-50))

def setsteer(demand): 
    pwm.setPWM(0,0,310+((demand-5)*20))  

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)
    def prints(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
    def indent(self):
        self.x += 10
    def unindent(self):
        self.x -= 10

#initialise variables
speeddemand=50
steerdemand=5
setspeed(speeddemand)
setsteer(steerdemand)
done=False
textPrint=TextPrint()

#main loop
while done==False:
    command=comsocket.myreceive(3)
    if command != '0':
        if command[0]=='0':  #steering command
            steerdemand=int(command[1])
            setsteer(steerdemand)
        if command[0]=='1':  #speed command
            speeddemand=int(command[1:3])
            setspeed(speeddemand)
 
    # display status
    screen.fill(WHITE)
    textPrint.reset()
    textPrint.prints(screen,"Steering: {}".format(steerdemand))    
    textPrint.prints(screen,"Speed: {}".format(speeddemand))
    pygame.display.flip()
    clock.tick(20)






