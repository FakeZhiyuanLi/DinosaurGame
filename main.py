import pygame
import os
import random

pygame.init()

# Variables

window = pygame.display.set_mode([1000, 400])

BG = (255, 246, 213)

# Obstacles
LITTLE_CACTUS = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Little_Cactus.png'))
BIG_CACTUS = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Big_Cactus.png'))
CACTUS_GROUP = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cactus_Group.png'))
BIRD = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Bird.py'))

# Background images
BG_LINE = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'BG_LINE.png'))
CLOUDS = pygame.image.load(os.path.join('DinosaurGame', 'Assets', 'Cloud.png'))

def HIGH_JUMP():
    print("High Jump")

def LOW_JUMP():
    print("Low Jump")

def DUCK():
    print("Duck")


def DRAW_WINDOW():
    window.fill(BG)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Space is high jump, and up arrow is low jump
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    HIGH_JUMP()
                if event.key == pygame.K_UP:
                    LOW_JUMP()
                if event.key == pygame.K_DOWN:
                    DUCK()

    

if __name__ == '__main__':
    main()