import pygame
import time
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
paddle_width = 50
paddle_height = 4
ball_pos_x = 5
ball_pos_y = 150
ball_radius = 10
fps = 0.015
move_x = 1
move_y = 1
rect_list = []
win_width = 300
win_height = 520
color=[red,green,blue]

screen = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('breakout')

game_exit = False
#gameloop
for j in range(5):
        for i in range(10):
            my_rect = pygame.Rect(30*i,5+25*j,28,24)
            rect_list.append(my_rect)
            

while not game_exit:
    if ball_pos_x + ball_radius == win_width:
        move_x = -1
    if ball_pos_x - ball_radius == 0:
        move_x = 1
    if ball_pos_y + ball_radius == win_height - 6 and ball_pos_x >= mouse_pos_x and ball_pos_x <= mouse_pos_x + paddle_width:
        move_y = -1
    if ball_pos_y - ball_radius == 0:
        move_y = 1
    
        
    if ball_pos_y + ball_radius >= win_height or len(rect_list)==0:
        game_exit = True
    
        
    for rect in rect_list:
        if rect.collidepoint(ball_pos_x,ball_pos_y-ball_radius-2):
            move_y = 1
            rect_list.remove(rect)
        
            
    ball_pos_x += move_x
    ball_pos_y += move_y
    time.sleep(fps)

    for event in pygame.event.get():
        mouse_pos_x = pygame.mouse.get_pos()[0]

    screen.fill(black)
    for rect in rect_list:
        pygame.draw.rect(screen,random.choice(color),rect)
            
    pygame.draw.circle(screen, random.choice(color),[ball_pos_x,ball_pos_y], ball_radius)
    pygame.draw.rect(screen,white,(mouse_pos_x,514,paddle_width,paddle_height))
    pygame.display.update()
    

pygame.quit()


quit()
