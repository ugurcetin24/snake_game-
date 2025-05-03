import pygame
import sys

# Pygame'i başlat
pygame.init()

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

    screen.fill(black)  # Ekranı siyaha boya
    pygame.display.update()  # Ekranı güncelle
