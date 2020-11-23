import pygame
from collections import namedtuple


Position = namedtuple('Position', ['x', 'y'])


pygame.init()
pygame.font.init()

screen_size = Position(x=800, y=600)
screen = pygame.display.set_mode(screen_size)
game_speed = 1
circle_radius = 50


background = (232, 232, 232)
green = (100,133,75)


pygame.display.set_caption('João Victor - TP3 - Item 13')

circle_position_x = screen.get_width() // 2 - circle_radius
circle_position_y = screen.get_height() // 2 - circle_radius
direction = 'right'

def draw_circle(position: Position):
    pygame.draw.circle(screen, green, position, circle_radius)


running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background)

    if circle_position_x >= screen.get_width() - circle_radius:
        game_speed += 1
        direction = 'left'
    elif circle_position_x <= circle_radius:
        game_speed += 1
        direction = 'right'

    circle_position_x += game_speed if direction == 'right' else -game_speed

    draw_circle(Position(x=circle_position_x, y=circle_position_y))

    
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()