import pygame
successes, fails = pygame.init()
print(successes, fails)
pygame.display.set_mode((700, 500))
pygame.display.set_caption("cs younes game")

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
