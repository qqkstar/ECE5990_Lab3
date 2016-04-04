import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 50)
p.start(0)

duty = 7.17
p.ChangeDutyCycle(duty)
print "Clockwise Orientation: initial duty cycle is " + `duty`
time.sleep(3)
for x in range(10):
  duty -= 0.04
  p.ChangeDutyCycle(duty)
  print "Step #" + str(x+1) + ": The current duty cycle is " + `duty`
  time.sleep(3)

duty = 7.21
p.ChangeDutyCycle(duty)
print "Counter-clockwise Orientation: initial duty cycle is " + `duty`
time.sleep(3)
for x in range(10):
  duty += 0.04
  p.ChangeDutyCycle(duty)
  print "Step #" + str(x+1) + ": The current duty cycle is " + `duty`
  time.sleep(3)

p.stop()
GPIO.cleanup()
