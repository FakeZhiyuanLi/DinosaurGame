import pygame
import os
import random

pygame.init()

# Variables
WIDTH, HEIGHT = 1000, 400
window = pygame.display.set_mode([WIDTH, HEIGHT])

BG = (255, 255, 255)

# Obstacles
# LITTLE_CACTUS = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Little_Cactus.png'))
BIG_CACTUS = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cactus1.png')), (29, 50))
BIG_CACTI = []
# CACTUS_GROUP = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cactus_Group.png'))
BIRD0 = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Bird0.png'))
BIRD1 = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Bird1.png'))
BIRDS = []

# Dino walk cycles
DINO0 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dinosaur0.png')), (50, 50))
DINO1 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dinosaur1.png')), (50, 50))
DINO2 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dinosaur2.png')), (50, 50))
DINO_RECT = pygame.Rect(50, HEIGHT / 2 - 35, 50, 50)

DEATH_EVENT = pygame.USEREVENT + 1
DEADSAUR = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dead_Dinosaur.png')), (50, 50))

GROUND = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Ground.png'))
GROUND_RECT = pygame.Rect((0, HEIGHT / 2 - 35), (1200, 20))
GROUND_RECT2 = pygame.Rect((1200, HEIGHT / 2 - 35), (1200, 20))
# Background images
# BG_LINE = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'BG_LINE.png'))
# CLOUDS = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cloud.png'))

clock = pygame.time.Clock()

def HIGH_JUMP():
    print("High Jump")

def LOW_JUMP():
    print("Low Jump")

def DUCK():
    print("Duck")

def HANDLE_GROUND(speed):
    GROUND_RECT.x = GROUND_RECT.x - speed
    GROUND_RECT2.x = GROUND_RECT2.x - speed

    if GROUND_RECT.x <= -1200:
        GROUND_RECT.x = 0

    if GROUND_RECT2.x <= 0:
        GROUND_RECT2.x = 1200

def GENERATE_OBSTACLE():
    x = random.randint(1, 2)
    if x == 1 or x == 2:
        BIG_CACTI.append(pygame.Rect(1100, HEIGHT / 2 - 50, 20, 50))

def CHECK_COLLISION():
    for cactus in BIG_CACTI:
        if DINO_RECT.colliderect(cactus):
            pygame.event.post(pygame.event.Event(DEATH_EVENT))
    
def DIE():
    window.fill(BG)
    
    window.blit(GROUND, (GROUND_RECT.x, HEIGHT / 2 - 15))
    window.blit(GROUND, (GROUND_RECT2.x, HEIGHT / 2 - 15))

    for cactus in BIG_CACTI:
        window.blit(BIG_CACTUS, (cactus.x, cactus.y))

    window.blit(DEADSAUR, (DINO_RECT.x, DINO_RECT.y))

    pygame.display.update()

def DRAW_WINDOW(cycle_iterations, speed):
    window.fill(BG)
    
    window.blit(GROUND, (GROUND_RECT.x, HEIGHT / 2 - 15))
    window.blit(GROUND, (GROUND_RECT2.x, HEIGHT / 2 - 15))

    for cactus in BIG_CACTI:
        cactus.x -= speed
        window.blit(BIG_CACTUS, (cactus.x, cactus.y))

    if DINO_RECT.y < 150:
        window.blit(DINO0, (DINO_RECT.x, DINO_RECT.y))
    else:
        if cycle_iterations == 1:
            window.blit(DINO1, (DINO_RECT.x, DINO_RECT.y))
        if cycle_iterations == 2:
            window.blit(DINO2, (DINO_RECT.x, DINO_RECT.y))

    pygame.display.update()

def main():
    running = True
    cycle_iterations = 1
    timing = 0
    speed = 5
    score = 0
    time_between_score = 10
    MOVEMENT = 0
    TIME_BETWEEN_OBSTACLE = 180
    time_between = 0
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == DEATH_EVENT:
                DIE()
                pygame.time.delay(2000)
                running = False
                break

            if event.type == pygame.KEYDOWN:
                # Space is high jump, and up arrow is low jump
                if event.key == pygame.K_SPACE and DINO_RECT.y >= 150 or event.key == pygame.K_w and DINO_RECT.y >= 150:
                    MOVEMENT = 18
                    time_between = 25
                if event.key == pygame.K_UP and DINO_RECT.y >= 150:
                    MOVEMENT = 15
                    time_between = 22
                if event.key == pygame.K_DOWN:
                    DUCK()
        timing += 1
        if timing % 6 == 0:
            cycle_iterations += 1
            if cycle_iterations >= 3:
                cycle_iterations -= 2
        if timing % 300 == 0:
            TIME_BETWEEN_OBSTACLE -= 15
            speed += 1

        if score % 100 == 0 and time_between_score > 1:
            time_between_score -= 1

        if timing % time_between_score == 0:
            score += 1
            print(score)
            
        if timing % TIME_BETWEEN_OBSTACLE == 0:
            GENERATE_OBSTACLE()

        # Handling movement
        if MOVEMENT >= 0:
            DINO_RECT.y -= 9
            MOVEMENT -= 1

        if time_between >= 0:
            time_between -= 1
            DINO_RECT.y += 3

        if DINO_RECT.y < 150 and time_between < 0:
            DINO_RECT.y += 6
        CHECK_COLLISION()
        HANDLE_GROUND(speed)
        DRAW_WINDOW(cycle_iterations, speed)


if __name__ == '__main__':
    main()
