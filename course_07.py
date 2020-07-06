import pygame
successes, fails = pygame.init()
print(successes, fails)

move_right = [pygame.image.load("hero/R1.png"), pygame.image.load("hero/R2.png"), pygame.image.load("hero/R3.png"), pygame.image.load("hero/R4.png"), pygame.image.load("hero/R5.png"), pygame.image.load("hero/R6.png"), pygame.image.load("hero/R7.png"), pygame.image.load("hero/R8.png"), pygame.image.load("hero/R9.png")]
move_left = [pygame.image.load("hero/L1.png"), pygame.image.load("hero/L2.png"), pygame.image.load("hero/L3.png"), pygame.image.load("hero/L4.png"), pygame.image.load("hero/L5.png"), pygame.image.load("hero/L6.png"), pygame.image.load("hero/L7.png"), pygame.image.load("hero/L8.png"), pygame.image.load("hero/L9.png")]


bg = pygame.image.load("bg.jpg")
hero = pygame.image.load("hero/standing.png")

screenWidth = 700
screenHeight = 500
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("cs younes game")

BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 600
y = 400
width = 64
height = 64
step = 5
left = False
right = False
moves = 0

speed = 10
isJumping = False


def redrawGame():
    global moves

    screen.blit(bg, (0, 0))

    if left:
        screen.blit(move_left[moves // 2], (x, y))
        moves += 1
        if moves == 18:
            moves = 0
    elif right:
        screen.blit(move_right[moves // 2], (x, y))
        moves += 1
        if moves == 18:
            moves = 0
    else:
        screen.blit(hero, (x, y))


    pygame.display.update()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - step >= 0:
        x -= step
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x + width + step <= screenWidth:
        x += step
        right = True
        left = False
    else:
        right = False
        left = False
        moves = 0
    if not isJumping:
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
