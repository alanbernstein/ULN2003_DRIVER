from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, a, b, c, d):
        try:
            self.A = Pin(a, Pin.OUT)
            self.B = Pin(b, Pin.OUT)
            self.C = Pin(c, Pin.OUT)
            self.D = Pin(d, Pin.OUT)
        except ValueError:
            print("Invalid pins provided. Check the pinout of your microcontroller.")

        # Used to cycle through the pin combinations in clockwise & counterclockwise.
        self.A_value = [1, 0, 0, 1]
        self.B_value = [1, 1, 0, 0]
        self.C_value = [0, 1, 1, 0]
        self.D_value = [0, 0, 1, 1]
    
    def turn(self, direction: int, steps: int, delay: float = 0.002):
        if delay >= 0.002 and steps > 0:
            if direction == -1 or direction == 1:
                for step in range(steps):
                    i = 0
                    for i in range(4):
                        self.A.value(self.A_value[i*direction])
                        self.B.value(self.B_value[i*direction])
                        self.C.value(self.C_value[i*direction])
                        self.D.value(self.D_value[i*direction])
                        sleep(delay)
                        i+=direction
            else:
                print("The value of direction is not valid. Please change the value to 1 (clockwise) or -1 (counterclockwise) to resolve this error.")
        else:
            if delay < 0.002:
                print("The value of delay is smaller than 0.002. Please increase the value of delay to resolve this error.")
            if steps < 1:
                print("The value of steps is smaller than 1. Please increase the value of steps to resolve this error.")
            self.A.value(0)
            self.B.value(0)
            self.C.value(0)
            self.D.value(0)

