from machine import Pin, PWM

class Servo:
    def __init__(self, pin, freq=50):
        self.pwm = PWM(Pin(pin), freq=freq)
        self.pwm.duty(0)
   
    def angle_to_duty(self, angle):
        return int((angle /180)*100  + 30)
    
    def set_angle(self, angle):
        duty = self.angle_to_duty(angle)
        self.pwm.duty(duty)

    def off(self):
        self.pwm.deinit()
