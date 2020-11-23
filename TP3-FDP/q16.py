import math, pygame
from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])

pygame.init()
pygame.font.init()

screenSize = Position(x=800, y=600)
screen = pygame.display.set_mode(screenSize)


background = (232, 232, 232)
blue = (41, 59, 136)


pygame.display.set_caption('João Victor - TP3 - Item 16')


def draw_star(screen, color, sides, radius, position):
    points = []

    for n in range(sides * 2):
        rad = radius if n % 2 == 0 else radius // 2
        angle = (n * math.pi / sides) + (90 * math.pi / 60)

        point = (
            int(math.cos(angle) * rad + position[0]),
            int(math.sin(angle) * rad + position[1])
        )

        points.append(point)

    return pygame.draw.polygon(screen, color, points)



running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background)

    
    draw_star(screen, blue, 5, 100, [screen.get_width() // 2, screen.get_height() // 2])

    #
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()