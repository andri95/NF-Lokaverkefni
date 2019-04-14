# coding: latin-1
# If you are commenting in icelandic you need the line above.
import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_image
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_image
        self.rect = self.image.get_rect()


# myndir
player_image = pygame.image.load('myndir/spilamadur.png')
asteroid_image = pygame.image.load('myndir/bolti.png')
missile_image = pygame.image.load('myndir/missile.png')
bg = pygame.image.load('myndir/background.jpg')

WHITE = (255, 255, 255)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# sprite og groups.
asteroid_list = pygame.sprite.Group()
# Group to hold missiles
missile_list = pygame.sprite.Group()
# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(4):
    for column in range(8):
        block = Asteroid()  # Set a random location for the block
        block.rect.x = 150 + (column * 50)  # random.randrange(screen_width - 20)
        block.rect.y = 35 + (
                    i * 45)  # random.randrange(screen_height - 160)  # ekki l�ta asteroid-ana byrja of ne�arlega
        asteroid_list.add(block)
        all_sprites_list.add(block)

# Create a player block
player = Player()
player.rect.x = 320
player.rect.y = 380

all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0
speed = 1

# -------- Main Program Loop -----------
# We need to check out what happens when the player hits the space bar in order to "shoot".
# A new missile is created and gets it's initial position in the "middle" of the player.
# Then this missile is added to the missile sprite-group and also to the all_sprites group.
flags = False
while not done:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot = Missile()
                shot.rect.x = player.rect.x + 30
                shot.rect.y = player.rect.y - 15
                missile_list.add(shot)
                all_sprites_list.add(shot)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if player.rect.x < -60:
            player.rect.x = 700
        player.rect.x -= 5
    elif key[pygame.K_RIGHT]:
        if player.rect.x > 700:
            player.rect.x = - 60
        player.rect.x += 5
    # Below is another good example of Sprite and SpriteGroup functionality.
    # It is now enough to see if some missile has collided with some asteroid
    # and if so, they are removed from their respective groups.l
    # In other words:  A missile exploded and so did an asteroid.

    # See if the player block has collided with anything.
    pygame.sprite.groupcollide(missile_list, asteroid_list, True, True)

    # Missiles move at a constant speed up the screen, towards the enemy
    for shot in missile_list:
        shot.rect.y -= 5

    # All the enemies move down the screen at a constant speed
    for block in asteroid_list:
        if block.rect.x >= 680:
            speed = -2
            flags = True

        if block.rect.x <= 0:
            speed = 2

        if flags:
            for x in range(len(asteroid_list)):
                asteroid_list.sprites()[x].rect.y += 6
            for y in range(len(asteroid_list)):
                asteroid_list.sprites()[x].rect.y += 6
            flags = False

        block.rect.x += speed
        # print(block.rect.x)
    # Draw all the spites
    all_sprites_list.draw(screen)
    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
pygame.quit()