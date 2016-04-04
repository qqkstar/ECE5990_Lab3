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

right_direction = font.render("", 1, (255,250,255))
right_direction_pos = right_direction.get_rect()
right_direction_pos.centerx = 210
right_direction_pos.centery = 50

def left_direction_disp(text):
  left_direction = font.render(text, 1, (255,250,255))
  return left_direction

def right_direction_disp(text):
  right_direction = font.render(text, 1, (255,250,255))
  return right_direction

while 1:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      p = pygame.mouse.get_pos()
      if p[0]>130 and p[0]<190 and p[1]>110 and p[1]<180:
        sign_toggle ^= 1
      elif p[0]>150 and p[0]<170 and p[1]>210 and p[1]<230:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_1]:
        left.ChangeDutyCycle(7.61)
        left_duty = 7.61
        left_info = 'forward'
        left_direction = left_direction_disp('forward')
      elif pressed[pygame.K_2]:
        left.ChangeDutyCycle(0)
        left_duty = 0
        left_info = 'idle'
        left_direction = left_direction_disp('idle')
      elif pressed[pygame.K_3]:
        left.ChangeDutyCycle(6.77)
        left_duty = 6.77
        left_info = 'backward'
        left_direction = left_direction_disp('backward')
      elif pressed[pygame.K_8]:
        right.ChangeDutyCycle(6.77)
        right_duty = 6.77
        right_info = 'forward'
        right_direction = right_direction_disp('forward')
      elif pressed[pygame.K_9]:
        right.ChangeDutyCycle(0)
        right_duty = 0
        right_info = 'idle'
        right_direction = right_direction_disp('idle')
      elif pressed[pygame.K_0]:
        right.ChangeDutyCycle(7.61)
        right_duty = 7.61
        right_info = 'backward'
        right_direction = right_direction_disp('backward')
      elif pressed[pygame.K_w]:
        left.ChangeDutyCycle(7.41)
        left_duty = 7.41
        left_info = 'forward'
        left_direction = left_direction_disp('forward')
        right.ChangeDutyCycle(6.97)
        right_duty = 6.97
        right_info = 'forward'
        right_direction = right_direction_disp('forward')
      elif pressed[pygame.K_s]:
        left.ChangeDutyCycle(6.97)
        left_duty = 6.97
        left_info = 'backward'
        left_direction = left_direction_disp('backward')
        right.ChangeDutyCycle(7.41)
        right_duty = 7.41
        right_info = 'backward'
        right_direction = right_direction_disp('backward')
      elif pressed[pygame.K_x]:
        left.ChangeDutyCycle(0)
        left_duty = 0
        left_info = 'stopped'
        left_direction = left_direction_disp('stopped')
        right.ChangeDutyCycle(0)
        right_duty = 0
        right_info = 'stopped'
        right_direction = right_direction_disp('stopped')
      elif pressed[pygame.K_a]:
        left.ChangeDutyCycle(6.97)
        left_duty = 6.97
        left_info = 'backward'
        left_direction = left_direction_disp('backward')
        right.ChangeDutyCycle(6.97)
        right_duty = 6.97
        right_info = 'forward'
        right_direction = right_direction_disp('forward')
      elif pressed[pygame.K_d]:
        left.ChangeDutyCycle(7.41)
        left_duty = 7.41
        left_info = 'forward'
        left_direction = left_direction_disp('forward')
        right.ChangeDutyCycle(7.41)
        right_duty = 7.41
        right_info = 'backward'
        right_direction = right_direction_disp('backward')
      elif pressed[pygame.K_ESCAPE]:
        sys.exit()
    
  screen.fill(black)
  if sign_toggle:
    screen.blit(stop, stop_rect)
    left.ChangeDutyCycle(left_duty)
    right.ChangeDutyCycle(right_duty)
    left_direction = left_direction_disp(left_info)
    right_direction = right_direction_disp(right_info)
  else:
    screen.blit(go, go_rect)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
    left_direction = left_direction_disp('stopped')
    right_direction = left_direction_disp('stopped')
  screen.blit(left_text, left_text_pos)
  screen.blit(right_text, right_text_pos)
  screen.blit(quit_text, quit_text_pos)
  screen.blit(left_direction, left_direction_pos)
  screen.blit(right_direction, right_direction_pos)
  pygame.display.flip()
