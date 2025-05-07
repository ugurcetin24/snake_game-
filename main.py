import pygame
import sys

# Pygame'i başlat
pygame.init()

#yılanın başlangıç konumu
x = 300
y = 200

#hareket miktarı(başlangıçta hareketsiz)
x_change = 0
y_change = 0

#yılanın kare boyutu
snake_block = 10

# Ekran boyutu
width = 600
height = 400

# Oyun penceresini oluştur
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yılan Oyunu")

# Renkler (R, G, B)
black = (0, 0, 0)
green = (0, 255, 0)

# Ana oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0
    x += x_change
    y += y_change

    screen.fill(black)
    pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])
    pygame.display.update()
    
