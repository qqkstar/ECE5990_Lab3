import RPi.GPIO as GPIO
import time

def servo_control(servo, direction):
  if direction == 'forward':
    servo.ChangeDutyCycle(7.61)
  elif direction == 'backward':
    servo.ChangeDutyCycle(6.77)
  elif direction == 'idle':
    servo.ChangeDutyCycle(0)
  else:
    print "Direction entered is invalid!"

if __name__ == "__main__":
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(17, GPIO.OUT)
  GPIO.setup(22, GPIO.OUT)

  left = GPIO.PWM(17, 50)
  right = GPIO.PWM(22, 50)
  left.start(0)
  right.start(0)

  while True:
    command = raw_input("Enter servo(left or right) and direction(forward, backward, idle): ")
    if command == 'stop':
      break
    command = command.split()
    print command
    servo = eval(command[0])
    direction = command[1]
    servo_control(servo, direction)
  left.stop()
  right.stop()
  GPIO.cleanup()
