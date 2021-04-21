import pygame
import os

width, height = 990, 510
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gorg's Kool SpaceShooter 69420")
# pygame.display.set_icon("""E:\Some photos n wallpaers\pfp\kool pfp.jpg""")

# Some values
GREYISH_BLACK = (38, 38, 38)
FPS = 100 # Specify the FPS you want to fix here
Spaceship1 = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'SpaceShip.png'))
Spaceship2 = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'SpaceShip2.png'))

S1_W = 30
S1_H = 30

S2_W = 30
S2_H = 30
def draw_window(S1, S2):
  WIN.fill(GREYISH_BLACK)
  WIN.blit(Spaceship1, (S1.x, S1.y))
  WIN.blit(Spaceship2, (S2.x, S2.y))
  pygame.display.update()

def main():
    S1 = pygame.Rect(250, 230, S1_W, S1_H)
    S2 = pygame.Rect(693, 230, S2_W, S2_H)
    run =True
    clock = pygame.time.Clock()
     # Fixed FPS
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        This_key_is_pressed = pygame.key.get_pressed()       

        if This_key_is_pressed[pygame.K_UP]:
            S1.y -= 2
        if This_key_is_pressed[pygame.K_DOWN]:
            S1.y += 2
        if This_key_is_pressed[pygame.K_LEFT]:
            S1.x -= 2
        if This_key_is_pressed[pygame.K_RIGHT]:
            S1.x += 2
        
        
        # S1.x += 1
        # S2.x -= 1
        draw_window(S1, S2)
    pygame.quit()

if __name__ == '__main__':
    main()