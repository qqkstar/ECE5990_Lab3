import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.pwm(17, 50)
p.start(0)

duty = 7.14
p.ChangeDutyCycle(duty)
print "Initial duty cycle is " + `duty`
raw_input('Press enter to accelerate')
for x in range(9):
  duty -= 0.05
  p.ChangeDutyCycle(duty)
  print "The current duty is " + `duty`
  raw_input('Press enter to accelerate')

p.stop()
GPIO.cleanup()
