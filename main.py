import pygame
import random
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

score_font = pygame.font.SysFont('Comic Sans MS', 20)

# Variables
WIDTH, HEIGHT = 1000, 400
window = pygame.display.set_mode([WIDTH, HEIGHT])

BG = (255, 255, 255)
BLACK = (0, 0, 0)

BIG_CACTUS = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cactus1.png')), (29, 50))
BIG_CACTI = []

SMALL_CACTUS = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cactus1.png')), (14, 25))
SMALL_CACTI = []

CACTUS_GROUP = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'CactusGroup1.png')), (35, 29))
CACTI_GROUPS = []

BIRD0 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Bird0.png')), (42, 30))
BIRD1 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Bird1.png')), (42, 30))
BIRDS = []

# Dino walk cycles
DINO0 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dinosaur0.png')), (50, 50))
DINO1 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dinosaur1.png')), (50, 50))
DINO2 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dinosaur2.png')), (50, 50))
DINO_RECT = pygame.Rect(50, 150, 50, 50)

DUCKSAUR0 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Ducksaur0.png')), (54, 25))
DUCKSAUR1 = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Ducksaur1.png')), (54, 25))

DEATH_EVENT = pygame.USEREVENT + 1
DEADSAUR = pygame.transform.scale(pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Dead_Dinosaur.png')), (50, 50))

GROUND = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Ground.png'))
GROUND_RECT = pygame.Rect((0, HEIGHT / 2 - 35), (1200, 20))
GROUND_RECT2 = pygame.Rect((1200, HEIGHT / 2 - 35), (1200, 20))

clock = pygame.time.Clock()

# Sounds
JUMP_SOUND = pygame.mixer.Sound(os.path.join('DinosaurGame', 'Assets', 'Jump.mp3'))
SCORE_SOUND = pygame.mixer.Sound(os.path.join('DinosaurGame', 'Assets', 'Score.mp3'))
DIE_SOUND = pygame.mixer.Sound(os.path.join('DinosaurGame', 'Assets', 'Die.mp3'))

def HANDLE_GROUND(speed):
    GROUND_RECT.x = GROUND_RECT.x - speed
    GROUND_RECT2.x = GROUND_RECT2.x - speed

    if GROUND_RECT.x <= -1200:
        GROUND_RECT.x = 0

    if GROUND_RECT2.x <= 0:
        GROUND_RECT2.x = 1200

def GENERATE_OBSTACLE():
    x = random.randint(1, 4)
    if x == 1:
        BIG_CACTI.append(pygame.Rect(1100, HEIGHT / 2 - 50, 28, 47))
    elif x == 2:
        SMALL_CACTI.append(pygame.Rect(1100, HEIGHT / 2 - 30, 14, 23))
    elif x == 3:
        CACTI_GROUPS.append(pygame.Rect(1100, HEIGHT / 2 - 30, 34, 28))
    elif x == 4:
        BIRDS.append(pygame.Rect(1100, random.randint(50, 180), 38, 28))

def CHECK_COLLISION():
    for cactus in BIG_CACTI:
        if DINO_RECT.colliderect(cactus):
            pygame.event.post(pygame.event.Event(DEATH_EVENT))
    for cactus in SMALL_CACTI:
        if DINO_RECT.colliderect(cactus):
            pygame.event.post(pygame.event.Event(DEATH_EVENT))
    for cactus in CACTI_GROUPS:
        if DINO_RECT.colliderect(cactus):
            pygame.event.post(pygame.event.Event(DEATH_EVENT))
    for bird in BIRDS:
        if DINO_RECT.colliderect(bird):
            pygame.event.post(pygame.event.Event(DEATH_EVENT))

def DIE():
    window.fill(BG)
    
    window.blit(GROUND, (GROUND_RECT.x, HEIGHT / 2 - 15))
    window.blit(GROUND, (GROUND_RECT2.x, HEIGHT / 2 - 15))

    for cactus in BIG_CACTI:
        window.blit(BIG_CACTUS, (cactus.x, cactus.y))

    window.blit(DEADSAUR, (DINO_RECT.x, DINO_RECT.y))

    pygame.display.update()

def DRAW_WINDOW(cycle_iterations, speed, score, DUCKING):
    window.fill(BG)
    
    score_text = score_font.render(str(score), True, BLACK)
    window.blit(score_text, (WIDTH - 70, 20))

    window.blit(GROUND, (GROUND_RECT.x, HEIGHT / 2 - 15))
    window.blit(GROUND, (GROUND_RECT2.x, HEIGHT / 2 - 15))

    for cactus in BIG_CACTI:
        cactus.x -= speed
        cactus_rect = pygame.Rect(cactus.x, cactus.y, cactus.width, cactus.height)
        pygame.draw.rect(window, (144, 238, 144), cactus_rect)
        window.blit(BIG_CACTUS, (cactus.x, cactus.y))
        

    for cactus in SMALL_CACTI:
        cactus.x -= speed
        cactus_rect = pygame.Rect(cactus.x, cactus.y, cactus.width, cactus.height)
        pygame.draw.rect(window, (144, 238, 144), cactus_rect)
        window.blit(SMALL_CACTUS, (cactus.x, cactus.y))
        
        
    for cactus in CACTI_GROUPS:
        cactus.x -= speed
        cactus_rect = pygame.Rect(cactus.x, cactus.y, cactus.width, cactus.height)
        pygame.draw.rect(window, (144, 238, 144), cactus_rect)
        window.blit(CACTUS_GROUP, (cactus.x, cactus.y))
        
        
    for bird in BIRDS:
        bird.x -= speed
        bird_rect = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
        pygame.draw.rect(window, (144, 238, 144), bird_rect)
        if cycle_iterations == 1:
            window.blit(BIRD0, (bird.x, bird.y))
        if cycle_iterations == 2:
            window.blit(BIRD1, (bird.x, bird.y))
        
        
    temp_rect = pygame.Rect(DINO_RECT.x, DINO_RECT.y, DINO_RECT.width, DINO_RECT.height)
    pygame.draw.rect(window, (144, 238, 144), temp_rect)
    if DUCKING:
        if cycle_iterations == 1:
            window.blit(DUCKSAUR0, (DINO_RECT.x, DINO_RECT.y))
        if cycle_iterations == 2:
            window.blit(DUCKSAUR1, (DINO_RECT.x, DINO_RECT.y))
    else:
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
    time_between_score = 8
    MOVEMENT = 0
    TIME_BETWEEN_OBSTACLE = 180
    time_between = 0
    DUCKING = False
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == DEATH_EVENT:
                DIE_SOUND.play()
                DIE()
                pygame.time.delay(2000)
                running = False
                break

            if event.type == pygame.KEYDOWN:
                # Space is high jump, and up arrow is low jump
                if not DUCKING and event.key == pygame.K_SPACE and DINO_RECT.y >= 150 or event.key == pygame.K_w and DINO_RECT.y >= 150:
                    DINO_RECT.width = 50
                    DINO_RECT.height = 50
                    DINO_RECT.y = 150
                    MOVEMENT = 18
                    time_between = 25
                    JUMP_SOUND.play()
                if not DUCKING and event.key == pygame.K_UP and DINO_RECT.y >= 150:
                    DINO_RECT.width = 50
                    DINO_RECT.height = 50
                    DINO_RECT.y = 150
                    MOVEMENT = 15
                    time_between = 22
                    JUMP_SOUND.play()
                if event.key == pygame.K_DOWN and DINO_RECT.y >= 150:
                    if DUCKING:
                        DUCKING = False
                        DINO_RECT.width = 50
                        DINO_RECT.height = 50
                        DINO_RECT.y = 150
                    else:
                        DUCKING = True
                        DINO_RECT.width = 54
                        DINO_RECT.height = 25
                        DINO_RECT.y = 176
        timing += 1
        if timing % 6 == 0:
            cycle_iterations += 1
            if cycle_iterations >= 3:
                cycle_iterations -= 2
        if timing % 360 == 0:
            TIME_BETWEEN_OBSTACLE -= 10
            speed += 1

        if score % 100 == 0 and time_between_score > 3 and score > 5:
            SCORE_SOUND.play()
            time_between_score -= 1
            score += 1
        elif score % 100 == 0 and score >= 10:
            SCORE_SOUND.play()
            score += 1

        if timing % time_between_score == 0:
            score += 1
            
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
            DINO_RECT.y += 7
        CHECK_COLLISION()
        HANDLE_GROUND(speed)
        DRAW_WINDOW(cycle_iterations, speed, score, DUCKING)


if __name__ == '__main__':
    main()
