import pygame
import psutil
from collections import namedtuple
import platform
import cpuinfo


# Game init
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)
titulo = pygame.font.Font(None, 28)
maior_titulo = pygame.font.Font(None, 36)

# Coordinates
Coordinate = namedtuple('Coordinate', ['x', 'y'])

# Configs
screenSize = Coordinate(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

info = cpuinfo.get_cpu_info()

# Change title
pygame.display.set_caption('Tp3_João_Puchetti')

# Colors
background = (232,232,232)
backgroundContrast = (196,182,182)
darkBlue = (48,71,94)
white = (255,255,255)
black = (0,0,0)
darkGrey = (53,56,57)
white_white = (255,255,255)
red = (240,84,84)
red_red = (240,0,130)
LightGrey = (34,40,49)
colors = [background, black, darkBlue, darkGrey, white]

def memory_usage():
    memory = psutil.virtual_memory()
    memory_total = round(psutil.virtual_memory().total/(1024*1024*1024), 2)

    width = screen.get_width() - 2 * 20
    percentage_used = width * memory.percent/100

    pygame.draw.rect(screen, LightGrey, (20, 50, width, 45))
    pygame.draw.rect(screen, red_red, (20, 50, percentage_used, 45))
    text = font.render(f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", 1, darkBlue)
    screen.blit(text, (20, 30))
    
def mostra_uso_cpu():
  l_cpu_percent = psutil.cpu_percent(percpu=True)
  screen.fill(white_white)
  num_cpu = len(l_cpu_percent)
  x = y = 10
  desl = 10
  alt = screen.get_height() - 220
  larg = (screen.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
  d = x + desl
  posi = 20
  atual = psutil.cpu_freq(percpu=True)
  for i in l_cpu_percent:
            pygame.draw.rect(screen, red_red, (d, y, larg, alt))
            pygame.draw.rect(screen, darkGrey, 	(d, y, larg, (1-i/100)*alt))
            d = d + larg + desl
            text = font.render(f"{i}%", 1, darkGrey)
            screen.blit(text, (posi, 400))
            text = font.render(f"{(atual[0])[0]}Mhz", 1, darkGrey)
            screen.blit(text, (posi, 420))
            posi += 130
        
  # parte mais abaixo da tela e à esquerda
  
def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = round(psutil.cpu_freq().current/1000,1)
    width = screen.get_width() - 2 * 20
    percentage_used = width * cpu_percent/100
    atual = psutil.cpu_freq()

    text = font.render(f"Uso de CPU Média: {cpu_percent}%", 1, darkGrey)
    screen.blit(text, (20, 460))
    text5 = font.render(f"Atual: {atual[0]}Mhz, Min: {atual[1]}Mhz, Max: {atual[2]}Mhz.", 1, darkGrey)
    screen.blit(text5, (230, 460))
    text1 = font.render(f"Processador: {platform.processor()}.", 1, darkGrey)
    screen.blit(text1, (20, 500))
    text1 = font.render(f"Processador: {info['brand_raw']}.", 1, darkGrey)
    screen.blit(text1, (20, 480))
    text5 = font.render(f"Arquitetura: {info['arch']}.", 1, darkGrey)
    screen.blit(text5, (620, 480)) 
    text5 = font.render(f"Núcleos: {psutil.cpu_count()} (Físicos: {psutil.cpu_count(logical=False)}).", 1, darkGrey)
    screen.blit(text5, (620, 500))
    text5 = font.render(f"Bits: {info['bits']}.", 1, darkGrey)
    screen.blit(text5, (620, 520))
    text2 = font.render(f"Node: {platform.node()}.", 1, darkGrey)
    screen.blit(text2, (20, 520))
    text4 = font.render(f"Sistema: {platform.system()} ({platform.platform()}).", 1, darkGrey)
    screen.blit(text4, (20, 540))

def cpu_info():
    info = cpuinfo.get_cpu_info()
    for i in info:
        print(i, ":", info[i])
    
def disk_usage():
    hard_drive = psutil.disk_usage('.')
    hard_drive_percent = hard_drive.percent

    width = screen.get_width() - 2 * 20
    percentage_used = width * hard_drive_percent/100

    pygame.draw.rect(screen, LightGrey, (20, 375, width, 45))
    pygame.draw.rect(screen, red_red, (20, 375, percentage_used, 45))
    text = font.render(f"Uso de Disco: {hard_drive_percent}%", 1, darkGrey)
    screen.blit(text, (20, 355))
    diskusage = psutil.disk_usage('/')
    total = (f"Total:  {round(diskusage.total/(1024*1024*1024), 2)}GB")
    text = font.render(total , 1, darkGrey)
    screen.blit(text, (450, 430))
    emuso = (f"Em uso: {round(diskusage.used/(1024*1024*1024), 2)}GB")
    text1 = font.render(emuso, 1, darkGrey)
    screen.blit(text1, (20, 430))
    livre = (f"Livre: {round(diskusage.free/(1024*1024*1024), 2)}GB")
    text2 = font.render(livre, 1, darkGrey)
    screen.blit(text2, (600, 430))

def draw_ip_info():
    addr = psutil.net_if_addrs()['Ethernet'][0].address
    ip = psutil.net_if_addrs()['Ethernet'][1].address
    text = font.render(f"Seu IP é: {addr}", 1, darkGrey)
    screen.blit(text, (20, 550))
    text = font.render(f"IPV4 é: {ip}", 1, darkGrey)
    screen.blit(text, (20, 575))

def menu():
    memory = psutil.virtual_memory()
    memory_total = round(psutil.virtual_memory().total/(1024*1024*1024), 2)
    
    text = titulo.render(f"Memória", 1, red_red)
    screen.blit(text, (20, 10))
    text = font.render(f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", 1, darkGrey)
    screen.blit(text, (20, 30))
    
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = round(psutil.cpu_freq().current/1000,1)
    width = screen.get_width() - 2 * 20
    percentage_used = width * cpu_percent/100
    atual = psutil.cpu_freq()

    text = titulo.render(f"CPU", 1, red_red)
    screen.blit(text, (20, 60))
    text = font.render(f"Uso de CPU Média: {cpu_percent}%", 1, darkGrey)
    screen.blit(text, (20, 90))
    text5 = font.render(f"Atual: {atual[0]}Mhz, Min: {atual[1]}Mhz, Max: {atual[2]}Mhz.", 1, darkGrey)
    screen.blit(text5, (20, 120))
    text1 = font.render(f"Processador: {platform.processor()}.", 1, darkGrey)
    screen.blit(text1, (20, 150))
    text1 = font.render(f"Processador: {info['brand_raw']}.", 1, darkGrey)
    screen.blit(text1, (20, 180))
    text5 = font.render(f"Arquitetura: {info['arch']}.", 1, darkGrey)
    screen.blit(text5, (20, 210)) 
    
    hard_drive = psutil.disk_usage('.')
    hard_drive_percent = hard_drive.percent
    
    text = titulo.render(f"Disco", 1, red_red)
    screen.blit(text, (20, 240))
    text = font.render(f"Uso de Disco: {hard_drive_percent}%", 1, darkGrey)
    screen.blit(text, (20, 270))
    diskusage = psutil.disk_usage('/')
    total = (f"Total:  {round(diskusage.total/(1024*1024*1024), 2)}GB")
    text = font.render(total , 1, darkGrey)
    screen.blit(text, (20, 300))
    emuso = (f"Em uso: {round(diskusage.used/(1024*1024*1024), 2)}GB")
    text1 = font.render(emuso, 1, darkGrey)
    screen.blit(text1, (20, 330))
    livre = (f"Livre: {round(diskusage.free/(1024*1024*1024), 2)}GB")
    text2 = font.render(livre, 1, darkGrey)
    screen.blit(text2, (20, 360))
    
    addr = psutil.net_if_addrs()['Ethernet'][0].address
    ip = psutil.net_if_addrs()['Ethernet'][1].address
    text = titulo.render(f"IP", 1, red_red)
    screen.blit(text, (20, 470))
    text = font.render(f"Seu IP é: {addr}", 1, darkGrey)
    screen.blit(text, (20, 500))
    text = font.render(f"IPV4 é: {ip}", 1, darkGrey)
    screen.blit(text, (20, 530))
    
# Game loop
running = True
clock = pygame.time.Clock()
counter = 0
ativo = 0
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if counter == 60:
        # paint the screen
        screen.fill(white_white)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
              ativo += 1
            elif event.key == pygame.K_LEFT:
              ativo -= 1
        if ativo == 0:
            screen.fill(white_white)
            menu()
        if ativo < 0:
            screen.fill(white_white)
            ativo = 4
        elif ativo == 1:
            screen.fill(white_white)
            memory_usage()
        elif ativo == 2:
            screen.fill(white_white)
            mostra_uso_cpu()
            cpu_usage()
        elif ativo == 3:
            screen.fill(white_white)
            disk_usage()
        elif ativo == 4:
            screen.fill(white_white)
            draw_ip_info()
        elif ativo > 4:
            ativo = 0

        counter = 0

    # Update the display
    pygame.display.update()

    # Update the display
    clock.tick(150)
    counter += 1

pygame.display.quit()
