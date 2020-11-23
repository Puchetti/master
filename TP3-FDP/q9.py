import pygame 
from collections import namedtuple


Position = namedtuple('Position', ['x', 'y'])


pygame.init()
pygame.font.init()

screenSize = Position(x=800, y=600)
screen = pygame.display.set_mode(screenSize)


background = (232,232,232)
blue = (41,59,136)


pygame.display.set_caption('João Victor - TP3 - Item 09')

def draw_circle():
    pygame.draw.circle(screen, blue, (screen.get_width() // 2, screen.get_height() // 2), 50)


running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background)

    draw_circle()

    # Update the display
    pygame.display.update()

pygame.display.quit()