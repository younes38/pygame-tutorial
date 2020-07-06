import pygame
successes, fails = pygame.init()
print(successes, fails)

screenWidth = 700
heightScreen = 500

screen = pygame.display.set_mode((screenWidth, heightScreen))
pygame.display.set_caption("cs younes game")

BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 600
y = 200
width = 50
height = 50
step = 5

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + width + step <= screenWidth:
        x += step
    if keys[pygame.K_UP] and y - step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + height + step <= heightScreen:
        y += step

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()
