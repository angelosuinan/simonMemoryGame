from gpiozero import LED, Button
from time import sleep
class Memory(object):
    
    gamestart = LED(16)
    scoreButton =  Button(21)
    addScore = 0
    resetButton = Button(20)
    def __init__(self):
        with open('assets/test.txt', 'w+') as f:
            f.write("0")
        self.gamestart.on()
    def start(self):
        while True:
            with open('assets/run.txt', 'r') as f:
                if f.readline() == "0":
                    return
            if self.scoreButton.is_pressed:
                text = ''
                with open('assets/test.txt', 'r') as f:
                    text = f.readline()
                text= int(text)+1
                print (text, "DSDSD")
                with open('assets/test.txt', 'w+') as f:
                    f.write(str(text))
                sleep(0.5)
            if self.resetButton.is_pressed:
                with open('run.txt', 'w+') as f:
                    f.write("0")
    def offLed(self):
        self.gamestart.off()
