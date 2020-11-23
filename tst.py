import psutil
import pygame
from collections import namedtuple

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 32)

Coordinate = namedtuple('Coordinate', ['x', 'y'])

screenSize = Coordinate(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

background = (232,232,232)
backgroundContrast = (196,182,182)
darkBlue = (48,71,94)
white = (255,255,255)
black = (0,0,0)
darkGrey = (34,40,49)
red = (240,84,84)

def draw_memory_usage(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_cpu_usage(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_cpu_info(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_disk_usage(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_ip_info(self, position: Coordinate, color):
    """
    Este método desenha no pygame o IP atual do usuário
    """
    addr = psutil.net_if_addrs()['en0'][0].address
    text = font.render(f"Seu IP é: {addr}", 1, darkGrey)
    screen.blit(text, (20, 150))

running = True
clock = pygame.time.Clock()
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background)

    
    pygame.display.update()

    
    clock.tick(150)

pygame.display.quit()