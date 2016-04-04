from two_wheel import servo_control
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

left = GPIO.PWM(17, 50)
right = GPIO.PWM(22, 50)
left.start(0)
right.start(0)

servo_control(left, 'forward')
time.sleep(2)
servo_control(left, 'idle')
time.sleep(2)
servo_control(left, 'backward')
time.sleep(2)
left.stop()

servo_control(right, 'forward')
time.sleep(2)
servo_control(right, 'idle')
time.sleep(2)
servo_control(right, 'backward')
time.sleep(2)
right.stop()

GPIO.cleanup
