import pygame, os, time

# Window dimensions
width, height = 990, 510
# Window
WIN = pygame.display.set_mode((width, height))
# Game name
pygame.display.set_caption("Gorg's Kool SpaceShooter 69420")
# Game icon
ico = pygame.image.load(os.path.join('Assets', 'icon.jpg'))
pygame.display.set_icon(ico)
# pygame.display.set_icon("""E:\Some photos n wallpaers\pfp\kool pfp.jpg""")

# Some values
GREY = (38, 38, 38)
FPS = 120 # Specify the FPS you want to fix here
bulletSpeed = 8 # Speed of bullet
S_BULLETS = []
MAX_BULLETS = 4
ShipSpeed = 3 # Speed of the SpaceShip
bullet = pygame.image.load(os.path.join('Assets', 'bullet.png'))
Spaceship1 = pygame.image.load(os.path.join('Assets', 'SpaceShip.png')) # Spaceship1
Spaceship2 = pygame.image.load(os.path.join('Assets', 'SpaceShip2.png')) # Spaceship2
# SPACESHIP1 HITBOX
S1_W = 30
S1_H = 30
# SPACESHIP1 HITBOX
S2_W = 30
S2_H = 30
# bullet hitbox dimensions
BS_W = 20
BS_H = 20
# Loads all sprites
def draw_window(S1, S2, BS):
    WIN.fill(GREY)
    WIN.blit(bullet, (BS.x, BS.y))
    WIN.blit(Spaceship1, (S1.x, S1.y))
    WIN.blit(Spaceship2, (S2.x, S2.y))
    pygame.display.update()


# Controls to move Spaceship
def S1_control(This_key_is_pressed, S1, BS):
    if This_key_is_pressed[pygame.K_UP] and S1.y - ShipSpeed > 0:
        S1.y -= ShipSpeed
        BS.y -= ShipSpeed
    if This_key_is_pressed[pygame.K_DOWN] and S1.y + ShipSpeed + S1.height < height:
        S1.y += ShipSpeed
        BS.y += ShipSpeed
    if This_key_is_pressed[pygame.K_LEFT] and S1.x - ShipSpeed > 0:
        S1.x -= ShipSpeed
        BS.x -= ShipSpeed
    if This_key_is_pressed[pygame.K_RIGHT] and S1.x + ShipSpeed + S1.width < width:
        S1.x += ShipSpeed
        BS.x += ShipSpeed

def handle_bullets(S_BULLETS, S1):
    for bull in S_BULLETS:
        bull.x += bulletSpeed


# Main Function. This is where all the magic happens!
def main():
    MAX_BULLETS = 4
    S1 = pygame.Rect(250, 230, S1_W, S1_H)# SpaceShip1 hitbox
    S2 = pygame.Rect(693, 230, S2_W, S2_H)# SpaceShip2 hitbox
    BS =  pygame.Rect(S1.x , S1.y , 10, 5) # bullet hitbox
    run =True
    clock = pygame.time.Clock()
    # Fixed FPS
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # bullet control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(S_BULLETS) < MAX_BULLETS - 1:
                    S_BULLETS.append(BS)


                # if MAX_BULLETS == 0:
                #     time.sleep(1)
                #     MAX_BULLETS = 4
                # else:
                #     pass


        This_key_is_pressed = pygame.key.get_pressed()
        handle_bullets(S_BULLETS, S1)
        draw_window(S1, S2, BS)
        S1_control(This_key_is_pressed, S1, BS)
        # Bullet(event)
    pygame.quit()

if __name__ == '__main__':
    main()