from Stepper import Stepper
from time import sleep

EN_PIN  = 23
STP_PIN = 27
DIR_PIN = 22

stepper = Stepper(23, 27, 22)

def main():
  print("Setting Up...")
  stepper.step('left', 90)
  sleep(1)
  stepper.step('right', 180)

  print("Ran...")
  stepper.cleanupPins()


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    stepper.cleanupPins()
    print("interrupted...")
    pass
