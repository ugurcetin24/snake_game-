import pygame
import sys

# Pygame'i başlat
pygame.init()

# Pygame'in saatini başlat
clock = pygame.time.Clock()

# Yılanın başlangıç konumu
x = 300
y = 200

# Hareket miktarı (başlangıçta hareketsiz)
x_change = 0
y_change = 0

# Yılanın kare boyutu
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

# Yazı tipi ve skor değişkeni
font = pygame.font.SysFont("Arial", 25)
score = 0

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

    # Ekran dışına çıkma kontrolü
    if x < 0 or x >= width or y < 0 or y >= height:
        pygame.quit()
        sys.exit()

    # Skoru artır
    score += 1

    # Ekranı temizle
    screen.fill(black)

    # Yılanı çiz
    pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

    # Skoru yazdır
    score_text = font.render("Skor: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, [10, 10])

    # Pencereyi güncelle
    pygame.display.update()

    # FPS ayarı
    clock.tick(10)  # 10 fps
