from time import sleep
import RPi.GPIO as gpio


EN_PIN  = 23
STP_PIN = 27
DIR_PIN = 22

def setup():

  gpio.setmode(gpio.BCM)
		
  #set gpio pins
  gpio.setup(STP_PIN, gpio.OUT)
  gpio.setup(DIR_PIN, gpio.OUT)
  gpio.setup(EN_PIN, gpio.OUT)
  
  #set enable to high (i.e. power is NOT going to the motor)
  gpio.output(EN_PIN, True)
  # set 
  gpio.output(DIR_PIN, False)
  return

def run(direction, steps=3200, speed=1):

  gpio.output(EN_PIN, False) # activate motor

  stepCounter = 0
	
  # waitTime = 0.000001/speed #waitTime controls speed
  waitTime = .01

  if direction is 'left':
    gpio.output(DIR_PIN, True)

  while stepCounter < steps:
    #gracefully exit if ctr-c is pressed
    #exitHandler.exitPoint(True) #exitHandler.exitPoint(True, cleanGPIO)

    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(STP_PIN, True)
    sleep(waitTime)
    gpio.output(STP_PIN, False)
    sleep(waitTime)
    stepCounter += 1

    # once done, break
  
    #set enable to high (i.e. power is NOT going to the motor)
  gpio.output(EN_PIN, True)
  return

def main():
  print("Setting Up...")
  setup()
  print("Running Right...")
  run('right', 320, 1)
  sleep(.5)
  print("Running Left...")
  run('left', 320, 1)
  print("Ran...")
  gpio.cleanup()
  print("Cleaned Up...")
  return

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    gpio.cleanup()
    print("interrupted...")
    pass
