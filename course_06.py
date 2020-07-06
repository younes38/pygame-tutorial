import pygame
successes, fails = pygame.init()
print(successes, fails)

bg = pygame.image.load("bg.jpg")
hero = pygame.image.load("hero/standing.png")

screenWidth = 700
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("cs younes game")

BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 600
y = 400
width = 50
height = 50
step = 5

speed = 10
isJumping = False


def redrawGame():
    screen.blit(bg, (0, 0))
    screen.blit(hero, (x, y))
    pygame.display.update()
while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + width + step <= screenWidth:
        x += step
    if not isJumping:
        if keys[pygame.K_UP] and y - step >= 0:
            y -= step
        if keys[pygame.K_DOWN] and y + height + step <= screenHeight:
            y += step
        if keys[pygame.K_SPACE]:
            isJumping = True
    else:
        if speed >= -10 :
            neg = 1
            if speed < 0:
                neg = -1
            y -= (speed ** 2) * 0.25 * neg
            speed -= 1
        else:
            speed = 10
            isJumping = False

    redrawGame()
