from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, a, b, c, d):
        self.A = Pin(a, Pin.OUT)
        self.B = Pin(b, Pin.OUT)
        self.C = Pin(c, Pin.OUT)
        self.D = Pin(d, Pin.OUT)

        self.pins = {
            0 : self.A,
            1 : self.B,
            2 : self.C,
            3 : self.D
            }
    def clockwise(self, steps, delay):
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
            self.D.value(1)
            self.A.value(1)
            sleep(delay)
            self.D.value(0)
            self.A.value(0)
            sleep(delay)
    def counterclockwise(self, steps, delay):
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
    
    def deinit():
        i=0
        while i <= 3:
            self.pins.value(0)
            i+=1
