import pygame
successes, fails = pygame.init()
print(successes, fails)

screenWidth = 700
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("cs younes game")

BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 100
y = 200
width = 50
height = 50
step = 5

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()
