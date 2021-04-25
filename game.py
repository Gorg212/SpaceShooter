import pygame
import os

width, height = 990, 510
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gorg's Kool SpaceShooter 69420")
# pygame.display.set_icon("""E:\Some photos n wallpaers\pfp\kool pfp.jpg""")

# Some values
GREY = (38, 38, 38)
FPS = 100 # Specify the FPS you want to fix here
ShipSpeed = 3 # Speed of the SpaceShip
Spaceship1 = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'SpaceShip.png')) # Spaceship1
Spaceship2 = pygame.image.load(os.path.join('SpaceShooter', 'Assets', 'SpaceShip2.png')) # Spaceship2
# SPACESHIP1 HITBOX
S1_W = 30
S1_H = 30
# SPACESHIP1 HITBOX
S2_W = 30
S2_H = 30
# Loads all sprites
def draw_window(S1, S2):
  WIN.fill(GREY)
  WIN.blit(Spaceship1, (S1.x, S1.y))
  WIN.blit(Spaceship2, (S2.x, S2.y))
  pygame.display.update()

# Controls to move Spaceship
def S1_control(This_key_is_pressed, S1):
    if This_key_is_pressed[pygame.K_UP] and S1.y - ShipSpeed > 0:
        S1.y -= ShipSpeed
    if This_key_is_pressed[pygame.K_DOWN] and S1.y + ShipSpeed + S1.height < height:
        S1.y += ShipSpeed
    if This_key_is_pressed[pygame.K_LEFT] and S1.x - ShipSpeed > 0:
        S1.x -= ShipSpeed
    if This_key_is_pressed[pygame.K_RIGHT] and S1.x + ShipSpeed + S1.width < width:
        S1.x += ShipSpeed


# Main Function. This is where all the magic happens!
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
        draw_window(S1, S2)
        S1_control(This_key_is_pressed, S1)
    pygame.quit()

if __name__ == '__main__':
    main()