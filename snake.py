#Snake by Jay-Dee

#import modules
import pygame
from pygame.locals import *
import random


pygame.init()

#create blank game window
screen_width = 600
screen_height = 600

#create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')


#define game variables
cell_size = 10
direction = 1 # 1 is up, 2 is right, 3 is down and 4 is left
update_snake = 0
food = [0,0]
new_food = True
new_piece = [0,0]
score = 0
game_over = False
clicked = False

#create snake
snake_bod = [[int(screen_width / 2 ), int(screen_height / 2)]]
snake_bod.append ([int(screen_width / 2 ), int(screen_height / 2) + cell_size])
snake_bod.append ([int(screen_width / 2 ), int(screen_height / 2) + cell_size * 2])
snake_bod.append ([int(screen_width / 2 ), int(screen_height / 2) + cell_size * 3])

# define colors
bg_color = (34, 35, 35)
body_inner = (61, 255, 152)
body_outer = (255, 74, 220)
food_col = (240, 246, 240)
snek_head = (255, 74, 220)
font_color = (255, 74, 220)
over_bg = (61, 255, 152)

#setup a rectangle for 'Play Again'
again_rect = Rect(screen_width // 2 -80, screen_height // 2, 160, 50)

#define font
font = pygame.font.SysFont(None, 40)

def draw_screen():
    screen.fill(bg_color)

def draw_score():
    score_txt = 'Score: ' + str(score)
    score_img = font.render(score_txt, True, font_color)
    screen.blit(score_img, (0,0))

def check_game_over(game_over):

    #first check if snake has eaten itself
    head_count = 0
    for segment in snake_bod:
        if snake_bod[0] == segment and head_count > 0:
            game_over = True
        head_count += 1

    #check if snake has gone out of bounds
    if snake_bod[0][0] < 0 or snake_bod[0][0] > screen_width or snake_bod[0][1] < 0 or snake_bod[0][1] > screen_height:
        game_over = True
    return game_over

def draw_game_over():
    over_txt = 'Game Over!'
    over_img = font.render(over_txt, True, font_color)
    pygame.draw.rect(screen, over_bg, (screen_width // 2 - 80, screen_height // 2 -60, 160, 50))
    screen.blit(over_img, (screen_width // 2 - 80, screen_height // 2 - 50 ))
    
    again_txt = 'Try Again?'
    again_img = font.render(again_txt, True, over_bg)
    pygame.draw.rect(screen, font_color, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10 ))
    


#setup look with exit handler
run = True
while run:

    draw_screen()
    draw_score()
    
    #iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    #create food
    if new_food == True:
        new_food = False
        food[0] = cell_size * random.randint(0, (screen_width // cell_size) - 1)
        food[1] = cell_size * random.randint(0, (screen_height // cell_size) - 1)
        

    #draw food
    pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))

    #check if food has been eaten
    if snake_bod[0] == food:
        new_food = True
        #create a new piece of the snake
        new_piece = list(snake_bod[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 3:
            new_piece[1] -= cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        if direction == 4:
            new_piece[1] -= cell_size
        
        #attach new piece to the end of the snake
        snake_bod.append(new_piece)

        #increase score
        score += 1
    
    if game_over == False:
        if update_snake > 99:
            update_snake = 0
            snake_bod = snake_bod[-1:] + snake_bod[:-1]
            #heading up
            if direction == 1:
                snake_bod[0][0] = snake_bod[1][0]
                snake_bod[0][1] = snake_bod[1][1] - cell_size
            if direction == 3:
                snake_bod[0][0] = snake_bod[1][0]
                snake_bod[0][1] = snake_bod[1][1] + cell_size
            if direction == 2:
                snake_bod[0][1] = snake_bod[1][1]
                snake_bod[0][0] = snake_bod[1][0] + cell_size
            if direction == 4:
                snake_bod[0][1] = snake_bod[1][1]
                snake_bod[0][0] = snake_bod[1][0] - cell_size
            game_over = check_game_over(game_over)

    if game_over == True:
        draw_game_over()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            mouse_pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(mouse_pos):
                #reset variables
        #define game variables

                direction = 1 # 1 is up, 2 is right, 3 is down and 4 is left
                update_snake = 0
                food = [0,0]
                new_food = True
                new_piece = [0,0]
                score = 0
                game_over = False
                

                #create snake
                snake_bod = [[int(screen_width / 2 ), int(screen_height / 2)]]
                snake_bod.append ([int(screen_width / 2 ), int(screen_height / 2) + cell_size])
                snake_bod.append ([int(screen_width / 2 ), int(screen_height / 2) + cell_size * 2])
                snake_bod.append ([int(screen_width / 2 ), int(screen_height / 2) + cell_size * 3])



    #draw snake
    head = 1
    for x in snake_bod:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (x[0] + 1 , x[1], cell_size - 2, cell_size - 2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, snek_head, (x[0] + 1 , x[1], cell_size - 2, cell_size - 2))
            head = 0

    #update the display
    pygame.display.update()

    update_snake += 1
        

#end pygame
pygame.quit()

#create a snake and setup the snake list
