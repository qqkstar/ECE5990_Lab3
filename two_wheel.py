import RPi.GPIO as GPIO
import time

def servo_control(servo, direction):
  if servo == 'left':
    if direction == 'forward':
      left.ChangeDutyCycle(7.61)
    elif direction == 'backward':
      left.ChangeDutyCycle(6.77)
    elif direction == 'idle':
      left.ChangeDutyCycle(0)
    else:
      print "Direction entered is invalid!"
  elif str(servo) == 'right':
    if direction == 'forward':
      right.ChangeDutyCycle(6.77)
    elif direction == 'backward':
      right.ChangeDutyCycle(7.61)
    elif direction == 'idle':
      right.ChangeDutyCycle(0)
    else:
      print "Direction entered is invalid!"
  else:
    print "Servo entered is invalid!"

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
    servo = 
    direction = 
    servo_control(servo, direction)
  left.stop()
  right.stop()
  GPIO.cleanup()
