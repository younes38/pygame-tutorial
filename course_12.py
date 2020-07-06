import pygame
successes, fails = pygame.init()
print(successes, fails)

move_right = [pygame.image.load("hero/R1.png"), pygame.image.load("hero/R2.png"), pygame.image.load("hero/R3.png"), pygame.image.load("hero/R4.png"), pygame.image.load("hero/R5.png"), pygame.image.load("hero/R6.png"), pygame.image.load("hero/R7.png"), pygame.image.load("hero/R8.png"), pygame.image.load("hero/R9.png")]
move_left = [pygame.image.load("hero/L1.png"), pygame.image.load("hero/L2.png"), pygame.image.load("hero/L3.png"), pygame.image.load("hero/L4.png"), pygame.image.load("hero/L5.png"), pygame.image.load("hero/L6.png"), pygame.image.load("hero/L7.png"), pygame.image.load("hero/L8.png"), pygame.image.load("hero/L9.png")]

move_rightE = [pygame.image.load("enemy/R1E.png"), pygame.image.load("enemy/R2E.png"), pygame.image.load("enemy/R3E.png"), pygame.image.load("enemy/R4E.png"), pygame.image.load("enemy/R5E.png"), pygame.image.load("enemy/R6E.png"), pygame.image.load("enemy/R7E.png"), pygame.image.load("enemy/R8E.png"), pygame.image.load("enemy/R9E.png"), pygame.image.load("enemy/R10E.png"), pygame.image.load("enemy/R11E.png")]
move_leftE = [pygame.image.load("enemy/L1E.png"), pygame.image.load("enemy/L2E.png"), pygame.image.load("enemy/L3E.png"), pygame.image.load("enemy/L4E.png"), pygame.image.load("enemy/L5E.png"), pygame.image.load("enemy/L6E.png"), pygame.image.load("enemy/L7E.png"), pygame.image.load("enemy/L8E.png"), pygame.image.load("enemy/L9E.png"), pygame.image.load("enemy/L10E.png"), pygame.image.load("enemy/L10E.png")]




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
        self.height = height
        self.step = 5
        self.left = False
        self.right = False
        self.moves = 0
        self.speed = 10
        self.isJumping = False
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 10, self.width - 40, self.height - 10)

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
        self.hitbox = (self.x + 20, self.y + 10, self.width - 40, self.height - 10)
        pygame.draw.rect(screen, RED, self.hitbox, 2)

class Bullet:
    def __init__(self, x, y, radius, color, direction, step):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.step = step * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(self.x, self.y) ,self.radius)

class Enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = x
        self.step = 3
        self.moves = 0
        self.hitbox = (self.x + 20, self.y, self.width - 30, self.height)

    def draw(self, screen):
        self.move()
        if self.step < 0:
            screen.blit(move_leftE[self.moves // 2], (self.x, self.y))
            self.moves += 1
            if self.moves == 11 * 2:
                self.moves = 0
        else:
            screen.blit(move_rightE[self.moves // 2], (self.x, self.y))
            self.moves += 1
            if self.moves == 11 * 2:
                self.moves = 0




    def move(self):
        if self.step > 0:
            if self.x + self.step > self.end:
                self.step *= -1
            else:
                self.x += self.step
        else:
            if self.x - self.step < self.start:
                self.step *= -1
            else:
                self.x += self.step

        self.hitbox = (self.x + 20, self.y , self.width - 30, self.height)
        pygame.draw.rect(screen, RED, self.hitbox, 2)



man = Player(600, 400, 64, 64)
enemy = Enemy(100, 400, 64, 64, 500)


def redrawGame():
    global moves

    screen.blit(bg, (0, 0))
    enemy.draw(screen)
    man.draw(screen)

    for bullet in  bullets:
        bullet.draw(screen)

    pygame.display.update()
bullets = []

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if len(bullets) < 5:
                    direction = 0
                    if man.right:
                        direction = 1
                    else:
                        direction = -1
                    bullets.append(
                        Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, RED, direction, 10))
    keys = pygame.key.get_pressed()

    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.step
        else:
            bullets.remove(bullet)





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
