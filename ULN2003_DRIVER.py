#from machine import Pin
from time import sleep

class Pin(object):
    IN = 0
    OUT = 1
    type_map = {0: "input", 1: "output"}
    def __init__(self, pin_number, pin_type):
        self.pin_number = pin_number
        self.pin_type = pin_type
    
    def value(self, val):
        print(f"<output {val} on {self.type_map[self.pin_type]} pin {self.pin_number}>")

class ULN2003:
    def __init__(self, motor_pin_id_groups):
        try:
            self.motor_pin_id_groups = motor_pin_id_groups
            self.motors = [[Pin(idx, Pin.OUT) for idx in group] for group in self.motor_pin_id_groups]
        except ValueError:
            print("Invalid pins provided. Check the pinout of your microcontroller.")

        # Used to cycle through the pin combinations in clockwise & counterclockwise.
        self.drive_values = [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
    
    def turn(self, motor_id: int, direction: int, steps: int, delay: float = 0.002):
        if delay >= 0.002 and steps > 0:
            if direction == -1 or direction == 1:
                for step in range(steps):
                    #print(f"step: {step}")
                    i = 0
                    for i in range(4):
                        #print(f"i: {i}")
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


def test_turn():
    driver = ULN2003([[1, 2, 3, 4], [5, 6, 7, 8]])
    tests = [(0, 1, 1), (0, -1, 1), (0, 1, 2), (0, -1, 2), (1, 1, 1), (1, -1, 1), (1, 1, 2), (1, -1, 2)]
    for idx, dir, steps in tests:
        print(f"{idx}, {dir}, {steps}")
        driver.turn(idx, dir, steps)
    driver.turn(1, 1, 1)
    driver.turn(1, -1, 1)
    driver.turn(1, 1, 2)
    driver.turn(1, -1, 2)

test_turn()