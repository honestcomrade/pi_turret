
from Stepper import Stepper

EN_PIN  = 23
STP_PIN = 27
DIR_PIN = 22

stepper = Stepper(23, 27, 22)

def main():
  print("Setting Up...")
  stepper.step('left', 1)
  print("Ran...")



if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("interrupted...")
    pass
