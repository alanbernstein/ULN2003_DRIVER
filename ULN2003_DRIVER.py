from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, motor_pin_id_groups):
        try:
            self.motor_pin_id_groups = motor_pin_id_groups
            self.motors = [[Pin(idx, Pin.OUT) for idx in group] for group in self.motor_pin_id_group]
        except ValueError:
            print("Invalid pins provided. Check the pinout of your microcontroller.")

        # Used to cycle through the pin combinations in clockwise & counterclockwise.
        self.drive_values = [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
    
    def turn(self, motor_id: int, direction: int, steps: int, delay: float = 0.002):
        if delay >= 0.002 and steps > 0:
            if direction == -1 or direction == 1:
                for step in range(steps):
                    i = 0
                    for i in range(4):
                        [pin.value(drive) for pin, drive in zip(self.motors[motor_id], self.drive_values)]
                        sleep(delay)
                        i+=direction
            else:
                print("The value of direction is not valid. Please change the value to 1 (clockwise) or -1 (counterclockwise) to resolve this error.")
        else:
            if delay < 0.002:
                print("The value of delay is smaller than 0.002. Please increase the value of delay to resolve this error.")
            if steps < 1:
                print("The value of steps is smaller than 1. Please increase the value of steps to resolve this error.")
            [pin.value(0) for pin in self.motors[motor_id]] # side effects inside a list comprehension is not the best form; may also not be supported by circuitpython
