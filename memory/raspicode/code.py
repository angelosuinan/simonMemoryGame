from gpiozero import LED, Button
from time import sleep
import pygame
class Memory(object):
    
    gamestart = LED(16)
    scoreButton =  Button(20)
    addScore = 0
    resetButton = Button(21)
    highscore = 0
    turnon = Button(26)
    def __init__(self):
        with open('assets/test.txt', 'w+') as f:
            f.write("0")
        self.gamestart.on()
        with open('assets/run.txt' , 'w+') as f:
            f.write("0")
    def start(self):
        #play mario musici
        with open('assets/run.txt', 'r') as f:
            if f.readline()=='f':
                return
        print('ytutyujtyjytjytjnfhnsfghngrhnfgngfhnhfghdgshth')
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        sound= pygame.mixer.Sound('raspicode/mario.ogg')
        sound.play(-1)
        with open('assets/run.txt' , 'w+') as f:
            f.write('f')
        while True:
            text=0
            if self.scoreButton.is_pressed:
                with open('assets/test.txt', 'r') as f:
                    text = f.readline()
                text= int(text)+1
                print (text, "DSDSD")
                with open('assets/test.txt', 'w+') as f:
                    f.write(str(text))
                sleep(0.2)
                if text > self.highscore:
                    self.highscore = text
                    print ("SDSDSDS")
                    with open('assets/high.txt', 'w+') as f:
                        f.write(str(text))
            if self.resetButton.is_pressed:
                    print ("malimaliamlia   EAQWEDWWQEQWEQW")
                    with open('assets/test.txt', 'w+') as f:
                        f.write("0")
                    sleep(0.2)
    def offLed(self):
        self.gamestart.off()
