from time import sleep
import RPi.GPIO as gpio

class Stepper:

  def __init__(self, en_pin, stp_pin, dir_pin, interval=.001):
    
    self.EN_PIN = en_pin
    self.STP_PIN = stp_pin
    self.DIR_PIN = dir_pin
    self.interval = interval
    # self.duration = duration
    self.__setup__()


  def __setup__(self):

    # set the gpio mode
    gpio.setmode(gpio.BCM)

    # set the pints to out mode
    gpio.setup(self.STP_PIN, gpio.OUT)
    gpio.setup(self.DIR_PIN, gpio.OUT)
    gpio.setup(self.EN_PIN, gpio.OUT)
    
    # set the Enable pin to high, disabling the motor
    gpio.output(self.EN_PIN, True)

  def step(self, direction, degrees=90):
    # activate motor
    gpio.output(self.EN_PIN, False)

    # set home position
    stepCounter = 0
    
    waitTime = self.interval

    # set the Direction pin
    if direction is "left":
      gpio.output(self.DIR_PIN, False)
    else:
      gpio.output(self.DIR_PIN, True)

    # 1.8 degrees per step
    steps = degrees / 1.8

    print('Total Steps:{}'.format(steps))

    while stepCounter < steps:
    
      gpio.output(self.STP_PIN, True)
      sleep(waitTime)
      gpio.output(self.STP_PIN, False)
      sleep(waitTime)
      stepCounter += 1  

    # disable the motor
    gpio.output(self.EN_PIN, True)
    

  def cleanupPins(self): 
    gpio.cleanup()
