import pygame, sys, math, time, uuid, random

def toint(i): return int(round(i))

frameWidth = 2000.0
frameHeight = 1200.0
windowScale = 0.8
frameRate = 30
frameCounter = 0
maxFrameCount = 1000000000
winWidth = toint(frameWidth*windowScale)
winHeight = toint(frameHeight*windowScale)

def processEvents(events):
  #global key_input
  for event in events:
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit(0)

clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((toint(winWidth), toint(winHeight)))
pygame.display.set_caption('Camera test pattern')
screen = pygame.display.get_surface()
screen.set_colorkey((255, 0, 255))
pygame.font.init()
font = pygame.font.SysFont("monospace", toint(winHeight*0.1), bold=True)


numberrenders = []
for num in range(10):
    numberrenders.append(font.render("{}".format(num), False, (255,255,255)))

number = 0

while True:
    screen.fill((0,0,0))

    for i in range(toint(frameWidth/10)):
        for j in range(toint(frameHeight/10)):
            screen.blit(numberrenders[number], (i*toint(frameWidth/10), j*toint(frameHeight/10)))

    number = (number + 1) % 10

    processEvents(pygame.event.get())

    """ Draw everything to the screen """
    pygame.display.flip()

    """ Wait for next frame """
    clock.tick(frameRate)

    """ Tick onto next frame """
    frameCounter = (frameCounter + 1)%maxFrameCount

    if (frameCounter%30 == 0):
        print("fps: {}".format(clock.get_fps()))
