from two_wheel import servo_control
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

left = GPIO.PWM(17, 50)
right = GPIO.PWM(22, 50)
left.start(0)
right.start(0)

servo_control(str(left), str(forward))
time.sleep(2)
servo_control(str(left), str(idle))
time.sleep(2)
servo_control(str(left), str(backward))
time.sleep(2)
servo_control(str(right), str(forward))
time.sleep(2)
servo_control(str(right), str(idle))
time.sleep(2)
servo_control(str(right), str(backward))
time.sleep(2)

left.stop()
right.stop()
GPIO.cleanup
