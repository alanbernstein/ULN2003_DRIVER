from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, a, b, c, d):
        self.A = Pin(a, Pin.OUT)
        self.B = Pin(b, Pin.OUT)
        self.C = Pin(c, Pin.OUT)
        self.D = Pin(d, Pin.OUT)

        # Used to cycle through pins in clockwise and counterclockwise functions
        self.pins = {
            0 : self.A,
            1 : self.B,
            2 : self.C,
            3 : self.D
            4 : self.A
            }
    
    def clockwise(self, steps, delay):
        if delay >= 0.002: # It won't move if it's below 0.002 (tested to 0.00199)
            for s in range(steps):
                i = 0
                while i < 3:
                    self.pins[i].value(1)
                    self.pins[i+1].value(1)
                    sleep(delay)
                    self.pins[i].value(0)
                    self.pins[i+1].value(0)
                    i+=1
                    sleep(delay)
        else:
            i = 0
            while i < 4:
                self.pins[i].value(0)
                i+=1
    
    def counterclockwise(self, steps, delay):
        if delay >= 0.002:
            for s in range(steps):
                i = 3
                self.D.value(1)
                self.A.value(1)
                sleep(delay)
                self.D.value(0)
                self.A.value(0)
                while i > 0:
                    self.pins[i].value(1)
                    self.pins[i-1].value(1)
                    sleep(delay)
                    self.pins[i].value(0)
                    self.pins[i-1].value(0)
                    i-=1
                    sleep(delay)
        else:
            i = 0
            while i < 4:
                self.pins[i].value(0)
                i+=1
