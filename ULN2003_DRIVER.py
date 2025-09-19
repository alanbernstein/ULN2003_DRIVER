from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, motor_pin_id_group):
        try:
            self.motor_pin_id_group = motor_pin_id_group
            self.motor = [
                Pin(self.motor_pin_id_group[0], Pin.OUT),
                Pin(self.motor_pin_id_group[1], Pin.OUT),
                Pin(self.motor_pin_id_group[2], Pin.OUT),
                Pin(self.motor_pin_id_group[3], Pin.OUT),
            ]
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
                        self.motor[0].value(self.A_value[i*direction])
                        self.motor[1].value(self.B_value[i*direction])
                        self.motor[2].value(self.C_value[i*direction])
                        self.motor[3].value(self.D_value[i*direction])
                        sleep(delay)
                        i+=direction
            else:
                print("The value of direction is not valid. Please change the value to 1 (clockwise) or -1 (counterclockwise) to resolve this error.")
        else:
            if delay < 0.002:
                print("The value of delay is smaller than 0.002. Please increase the value of delay to resolve this error.")
            if steps < 1:
                print("The value of steps is smaller than 1. Please increase the value of steps to resolve this error.")
            self.motor[0].value(0)
            self.motor[1].value(0)
            self.motor[2].value(0)
            self.motor[3].value(0)