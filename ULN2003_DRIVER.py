from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, a, b, c, d):
        self.A = Pin(a, Pin.OUT)
        self.B = Pin(b, Pin.OUT)
        self.C = Pin(c, Pin.OUT)
        self.D = Pin(d, Pin.OUT)

        # Used to cycle through pins in clockwise and counterclockwise functions
        self.A_value = [1, 0, 0, 1]
        self.B_value = [1, 1, 0, 0]
        self.C_value = [0, 1, 1, 0]
        self.D_value = [0, 0, 1, 1]
    
    def clockwise(self, steps, delay):
        if delay >= 0.002: # It won't move if it's below 0.002 (tested to 0.00199)
            for s in range(steps):
                i = 0
                while i < 4:
                    self.A.value(self.A_value[i])
                    self.B.value(self.A_value[i])
                    self.C.value(self.A_value[i])
                    self.D.value(self.A_value[i])
                    sleep(delay)
                    i+=1
        else:
            self.A.value(0)
            self.B.value(0)
            self.C.value(0)
            self.D.value(0)
    
    def counterclockwise(self, steps, delay):
        if delay >= 0.002:
            for s in range(steps):
                i = 3
                while i >= 0:
                    self.A.value(self.A_value[i])
                    self.B.value(self.A_value[i])
                    self.C.value(self.A_value[i])
                    self.D.value(self.A_value[i])
                    sleep(delay)
                    i-=1
        else:
            self.A.value(0)
            self.B.value(0)
            self.C.value(0)
            self.D.value(0)
