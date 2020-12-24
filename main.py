import pygame
import sys
import pygame.font
import time
import random
import math

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
pygame.font.init()

snake_block = 20
snake_speed = 10

lost = False
pygame.init()
pygame.font.init()
global SCREEN
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(WHITE)

pygame.display.set_caption("Euan's Snake Game in Python")

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font_style = pygame.font.Font(None, 50)

def message(msg, color, textx, texty):
    msg = font_style.render(msg, True, color)
    SCREEN.blit(msg, [textx, texty])


def drawGrid():
    cell_amount = 20
    SCREEN.fill(WHITE)
    for x in range(SCREEN_WIDTH // cell_amount):
        for y in range(SCREEN_HEIGHT // cell_amount):
            rect = pygame.Rect(x * cell_amount, y * cell_amount, cell_amount, cell_amount)  #Define 1 cell
            pygame.draw.rect(SCREEN, BLACK, rect, 1)    #Draw each cell

def foodLocation():
    global foodx, foody
    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foodx = (math.ceil(foodx / 20) * 20)
    foody = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = (math.ceil(foody / 20) * 20)
foodLocation()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(SCREEN, BLACK, [x[0], x[1], snake_block, snake_block])

def mainLoop():
    lost = False
    game_over = False
    score = 0
    x = 200
    y = 200
    x_change = 0
    y_change = 0
    clock = pygame.time.Clock()
    snake_List = []
    Length_of_snake = 0
    snake_speed = 10
    while lost == False:     # Main Loop
        while game_over:
            SCREEN.fill(BLACK)
            message("You Lost! Press C-Play Again or Q-Quit", WHITE, 0, 0)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        mainLoop()
                        mainLoop()

        for event in pygame.event.get():    ##Get key input
            if event.type == pygame.QUIT:
                lost = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        x += x_change   #Move head
        y += y_change
        drawGrid()

        pygame.draw.rect(SCREEN, BLACK, [x, y, 20, 20])
        pygame.draw.rect(SCREEN, RED, [foodx, foody, snake_block, snake_block]) #Draw food for the snake
        pygame.draw.rect(SCREEN, BLACK, [x, y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)


        our_snake(snake_block, snake_List)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        message(format(score), BLACK, 0, 0)
        pygame.display.update()
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        if x > SCREEN_WIDTH or x < 0 or y > SCREEN_HEIGHT or y < 0:
            game_over = True

        if x == foodx and y == foody:
            foodLocation()
            Length_of_snake += 1
            score += 1
            snake_speed += 1
        clock.tick(snake_speed)

        for i in snake_List[:-1]:
            if i == snake_Head:
                game_over = True
mainLoop()