import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 50)
p.start(0)
time.sleep(2)

p.ChangeDutyCycle(7.17)
print "Clockwise Orientation: Initialize"
time.sleep(5)

p.ChangeDutyCycle(6.97)
print "Clockwise Orientation: Half Speed" 
time.sleep(5)

p.ChangeDutyCycle(6.77)
print "Clockwise Orientation: Full Speed"
time.sleep(5)

p.ChangeDutyCycle(0)
time.sleep(2)

p.ChangeDutyCycle(7.21)
print "Counter-clockwise Orientation: Initialize"
time.sleep(5)

p.ChangeDutyCycle(7.41)
print "Counter-clockwise Orientation: Half Speed" 
time.sleep(5)

p.ChangeDutyCycle(7.61)
print "Counter-clockwise Orientation: Full Speed"
time.sleep(5)

p.stop()
GPIO.cleanup()
