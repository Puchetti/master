import pygame
import psutil
from collections import namedtuple
import platform

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)

Coordinate = namedtuple('Coordinate', ['x', 'y'])

screenSize = Coordinate(x=700, y=500)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Monitor de Atividades')

background = (232,232,232)
backgroundContrast = (196,182,182)
darkBlue = (48,71,94)
white = (255,255,255)
black = (0,0,0)
darkGrey = (34,40,49)
red = (240,84,84)
colors = [background, black, darkBlue, darkGrey, white]

def draw_ip_info():
    addr = psutil.net_if_addrs()['Ethernet'][0].address
    ip = psutil.net_if_addrs()['Ethernet'][1].address
    text = font.render(f"Seu IP é: {addr}", 1, darkGrey)
    screen.blit(text, (20, 450))
    text = font.render(f"IPV4 é: {ip}", 1, darkGrey)
    screen.blit(text, (20, 470))
 
def memory_usage():
    memory = psutil.virtual_memory()
    memory_total = round(psutil.virtual_memory().total/(1024*1024*1024), 2)
    
    width = screen.get_width() - 2 * 20
    percentage_used = width * memory.percent/100

    pygame.draw.rect(screen, backgroundContrast, (20, 50, width, 70))
    pygame.draw.rect(screen, darkBlue, (20, 50, percentage_used, 70))
    text = font.render(f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", 1, darkBlue)
    screen.blit(text, (20, 30))

def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)

    width = screen.get_width() - 2 * 20
    percentage_used = width * cpu_percent/100

    pygame.draw.rect(screen, backgroundContrast, (20, 170, width, 70))
    pygame.draw.rect(screen, darkGrey, (20, 170, percentage_used, 70))
    text = font.render(f"Uso de CPU: {cpu_percent}%", 1, darkGrey)
    screen.blit(text, (20, 150))
    text1 = font.render(f"Processador: {platform.processor()}.", 1, darkGrey)
    screen.blit(text1, (20, 240))

def disk_usage():
    hard_drive = psutil.disk_usage('.')
    hard_drive_percent = hard_drive.percent

    width = screen.get_width() - 2 * 20
    percentage_used = width * hard_drive_percent/100

    pygame.draw.rect(screen, backgroundContrast, (20, 320, width, 70))
    pygame.draw.rect(screen, darkBlue, (20, 320, percentage_used, 70))
    text = font.render(f"Uso de Disco: {hard_drive_percent}%", 1, darkBlue)
    screen.blit(text, (20, 300))

running = True
clock = pygame.time.Clock()
counter = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if counter == 60:
        screen.fill(background)
        memory_usage()
        cpu_usage()
        disk_usage()
        draw_ip_info()
        counter = 0

    pygame.display.update()

    clock.tick(150)
    counter += 1

pygame.display.quit()