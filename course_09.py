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

BLACK = (0, 0, 0)  # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.weight = height
        self.step = 5
        self.left = False
        self.right = False
        self.moves = 0
        self.speed = 10
        self.isJumping = False
        self.standing = True

    def draw(self, screen):
        if not self.standing:
            if self.left:
                screen.blit(move_left[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 18:
                    self.moves = 0
            elif self.right:
                screen.blit(move_right[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 18:
                    self.moves = 0
        else:
            if self.right:
                screen.blit(move_right[0], (self.x, self.y))
            else:
                screen.blit(move_left[0], (self.x, self.y))


man = Player(600, 400, 64, 64)


def redrawGame():
    global moves

    screen.blit(bg, (0, 0))
    man.draw(screen)
    pygame.display.update()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x - man.step >= 0:
        man.x -= man.step
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x + man.width + man.step <= screenWidth:
        man.x += man.step
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.moves = 0
    if not man.isJumping:
        if keys[pygame.K_SPACE]:
            man.isJumping = True
    else:
        if man.speed >= -10 :
            neg = 1
            if man.speed < 0:
                neg = -1
            man.y -= (man.speed ** 2) * 0.25 * neg
            man.speed -= 1
        else:
            man.speed = 10
            man.isJumping = False

    redrawGame()
