import pygame
import random

pygame.init()
#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
#Window
screen_width = 900
screen_heigth = 600
gameWindow = pygame.display.set_mode((screen_width,screen_heigth))
#Game title
pygame.display.set_caption("Dev")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])

#Game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(60, screen_heigth-20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 60 #frames per second
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game over! Press Enter to contiue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()