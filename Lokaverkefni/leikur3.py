import random
import pygame


#Litir
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
#Myndir
#"nafn æa myndinni" = pygame.image.load('path/name.png')
geimskip = pygame.image.load("Myndir/geimskip.png")
skot = pygame.image.load("Myndir/skot.png")

#basic
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pew Pew')
size = 800,600
screen = pygame.display.set_mode(size)
#erfit mjög fokking erfitt
geimskip_top = screen.get_height() - geimskip.get_height()
geimskip_left = screen.get_width()/2 - geimskip.get_width()/2

x=375

shoot_y=0

running = True
while running == True:
    clock.tick(60)
    screen.fill(black)
    screen.blit(geimskip,(x-geimskip.get_width()/2,geimskip_top))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                    x = x - 10
            elif event.key == pygame.K_d:
                    x = x + 10
            elif event.key == pygame.K_SPACE:
                    shoot_y = 500
                    shoot_x = x
    if shoot_y >0:
        screen.blit(skot,(shoot_x,shoot_y))
        shoot_y -=10


#    for i in range(0, 5):
 #       dice[i] = random.randint(0, 5)
  #      window.blit(sd[dice[i]],(posDiceX[i],posDiceY[i]))
#    https://pythonprogramming.net / displaying - images - pygame /

    pygame.display.update()

pygame.quit()
quit()
