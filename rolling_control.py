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

while 1:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      p = pygame.mouse.get_pos()
      if p[0]>130 and p[0]<190 and p[1]>110 and p[1]<180:
        #sys.exit()
        sign_toggle ^= 1
      else:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_1]:
        left.ChangeDutyCycle(7.61)
      elif pressed[pygame.K_2]:
        left.ChangeDutyCycle(0)
      elif pressed[pygame.K_3]:
        left.ChangeDutyCycle(6.77)
      elif pressed[pygame.K_8]:
        right.ChangeDutyCycle(6.77)
      elif pressed[pygame.K_9]:
        right.ChangeDutyCycle(0)
      elif pressed[pygame.K_0]:
        right.ChangeDutyCycle(7.61)

  screen.fill(black)
  if sign_toggle:
    screen.blit(stop, stop_rect)
  else:
    screen.blit(go, go_rect)
  screen.blit(left_text, left_text_pos)
  screen.blit(right_text, right_text_pos)
  pygame.display.flip()
