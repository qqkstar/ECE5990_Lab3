import RPi.GPIO as GPIO
import time, sys, os
import pygame

os.environ['SDL_VIDEODRIVER'] = 'fbcon'   #set up os environment to display to TFT
os.environ['SDL_FBDEV'] = '/dev/fb1'
os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen' #set up touchscreen as mouse input
os.environ['SDL_MOUSEDRV'] = 'TSLIB'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

left = GPIO.PWM(17, 50)
right = GPIO.PWM(22, 50)
left.start(0)
right.start(0)
left_duty = 0
right_duty = 0
left_info = 'idle'
right_info = 'idle'

black = 0, 0, 0

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

stop = pygame.image.load("stop.png")
stop = pygame.transform.scale(stop, (80, 80))
stop_rect = stop.get_rect()
stop_rect.centerx = 160
stop_rect.centery = 150

go = pygame.image.load("go.png")
go = pygame.transform.scale(go, (80, 80))
go_rect = stop.get_rect()
go_rect.centerx = 160
go_rect.centery = 150

sign_toggle = 1

font = pygame.font.Font(None, 18)

left_text = font.render("LEFT MOTOR:", 1, (255,250,255))
left_text_pos = left_text.get_rect()
left_text_pos.centerx = 70
left_text_pos.centery = 30

right_text = font.render("RIGHT MOTOR:", 1, (255,250,255))
right_text_pos = right_text.get_rect()
right_text_pos.centerx = 240
right_text_pos.centery = 30

quit_text = font.render("QUIT", 1, (255,250,255))
quit_text_pos = quit_text.get_rect()
quit_text_pos.centerx = 160
quit_text_pos.centery = 220

left_direction = font.render("", 1, (255,250,255))
left_direction_pos = left_direction.get_rect()
left_direction_pos.centerx = 40
left_direction_pos.centery = 50
left_direction_pos2 = left_direction.get_rect()
left_direction_pos2.centerx = 40
left_direction_pos2.centery = 70
left_direction_pos3 = left_direction.get_rect()
left_direction_pos3.centerx = 40
left_direction_pos3.centery = 90


right_direction = font.render("", 1, (255,250,255))
right_direction_pos = right_direction.get_rect()
right_direction_pos.centerx = 210
right_direction_pos.centery = 50
right_direction_pos2 = right_direction.get_rect()
right_direction_pos2.centerx = 210
right_direction_pos2.centery = 70
right_direction_pos3 = right_direction.get_rect()
right_direction_pos3.centerx = 210
right_direction_pos3.centery = 90



def left_direction_disp(text):
  left_direction = font.render(text, 1, (255,250,255))
  return left_direction

def right_direction_disp(text):
  right_direction = font.render(text, 1, (255,250,255))
  return right_direction

left.ChangeDutyCycle(7.41)
left_duty = 7.41
left_info = 'forward'
left_direction = left_direction_disp('forward')
right.ChangeDutyCycle(6.97)
right_duty = 6.97
right_info = 'forward'
right_direction = right_direction_disp('forward')

screen.fill(black)
screen.blit(go, go_rect)
screen.blit(left_text, left_text_pos)
screen.blit(right_text, right_text_pos)
screen.blit(quit_text, quit_text_pos)
screen.blit(left_direction, left_direction_pos)
screen.blit(right_direction, right_direction_pos)
pygame.display.flip()
time.sleep(4)

left.ChangeDutyCycle(7.41)
left_duty = 7.41
left_info = 'forward'
left_direction2 = left_direction_disp('forward')
right.ChangeDutyCycle(7.41)
right_duty = 7.41
right_info = 'backward'
right_direction2 = right_direction_disp('backward')

screen.fill(black)
screen.blit(go, go_rect)
screen.blit(left_text, left_text_pos)
screen.blit(right_text, right_text_pos)
screen.blit(quit_text, quit_text_pos)
screen.blit(left_direction, left_direction_pos)
screen.blit(right_direction, right_direction_pos)
screen.blit(left_direction2, left_direction_pos2)
screen.blit(right_direction2, right_direction_pos2)
pygame.display.flip()
time.sleep(3)

left.ChangeDutyCycle(6.97)
left_duty = 6.97
left_info = 'backward'
left_direction3 = left_direction_disp('backward')
right.ChangeDutyCycle(6.97)
right_duty = 6.97
right_info = 'forward'
right_direction3 = right_direction_disp('forward')

screen.fill(black)
screen.blit(go, go_rect)
screen.blit(left_text, left_text_pos)
screen.blit(right_text, right_text_pos)
screen.blit(quit_text, quit_text_pos)
screen.blit(left_direction, left_direction_pos)
screen.blit(right_direction, right_direction_pos)
screen.blit(left_direction2, left_direction_pos2)
screen.blit(right_direction2, right_direction_pos2)
screen.blit(left_direction3, left_direction_pos3)
screen.blit(right_direction3, right_direction_pos3)
pygame.display.flip()
time.sleep(3)

left.ChangeDutyCycle(6.97)
left_duty = 6.97
left_info = 'backward'
left_direction = left_direction_disp('backward')
right.ChangeDutyCycle(7.41)
right_duty = 7.41
right_info = 'backward'
right_direction = right_direction_disp('backward')

screen.fill(black)
screen.blit(go, go_rect)
screen.blit(left_text, left_text_pos)
screen.blit(right_text, right_text_pos)
screen.blit(quit_text, quit_text_pos)
screen.blit(left_direction, left_direction_pos)
screen.blit(right_direction, right_direction_pos)
screen.blit(left_direction2, left_direction_pos2)
screen.blit(right_direction2, right_direction_pos2)
screen.blit(left_direction3, left_direction_pos3)
screen.blit(right_direction3, right_direction_pos3)
pygame.display.flip()
time.sleep(3)

screen.blit(stop, stop_rect)
pygame.display.flip()
left.stop()
right.stop()
time.sleep(4)
sys.exit()
