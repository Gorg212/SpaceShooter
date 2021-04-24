import pygame
import os

WIDTH, HEIGHT = 990, 510
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gorg's Kool SpaceShooter 69420")

programIcon = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'icon.jpg'))
pygame.display.set_icon(programIcon)


# Some values
GREYISH_BLACK = (38, 38, 38)
FPS = 100 # Specify the FPS you want to fix here
Spaceship1 = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'SpaceShip.png'))
Spaceship2 = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'SpaceShip2.png'))

S1_W = 30
S1_H = 30
# ⬇⬆: HitBoxes
S2_W = 30
S2_H = 30

SHIPSPEED = 2

def draw_window(S1, S2):
  WIN.fill(GREYISH_BLACK)
  WIN.blit(Spaceship1, (S1.x, S1.y))
  WIN.blit(Spaceship2, (S2.x, S2.y))
  pygame.display.update()



def S1_control(This_key_is_pressed, S1):
    if This_key_is_pressed[pygame.K_UP] and S1.y - SHIPSPEED > 0:
        S1.y -= SHIPSPEED
    if This_key_is_pressed[pygame.K_DOWN] and S1.y + SHIPSPEED + S1.height < HEIGHT:
        S1.y += SHIPSPEED
    if This_key_is_pressed[pygame.K_LEFT] and S1.x - SHIPSPEED > 0:
        S1.x -= SHIPSPEED
    if This_key_is_pressed[pygame.K_RIGHT] and S1.x + SHIPSPEED + S1.width < WIDTH:
        S1.x += SHIPSPEED
        



def main():
    S1 = pygame.Rect(250, 230, S1_W, S1_H)
    S2 = pygame.Rect(693, 230, S2_W, S2_H)
    clock = pygame.time.Clock()
     # Fixed FPS
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        This_key_is_pressed = pygame.key.get_pressed() 
        draw_window(S1, S2)
        S1_control(This_key_is_pressed, S1)
    pygame.quit()



if __name__ == '__main__':
    main()