import pygame
from functions import load_image
import os
import subprocess

# взятие данных обьектов
with open("objects coordinates.txt", mode="r") as file:
    data = [l.split(";") for l in file.read().split("\n")]
character_view_coordinates = x1, y1, x2, y2 = list(map(int,
                                                       data[1][1].split(",")
                                                       )
                                                   )

size = width, height = list(map(int, data[0][2].split(",")))

# инициализация окна
pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Pump It Up💪💪💪")

# добавление фона
background_image = pygame.image.load('window.png')
window.blit(background_image, (0, 0))

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()

# обновление картинки персонажа
subprocess.run(["python", "make total character.py"])

# загрузка картинки персонажа
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = 'total_character.png'
sprite.image = load_image(file_path, character_view_coordinates)

# помещение персонажа в прямоугольник
sprite.rect = sprite.image.get_rect()
sprite.rect.x, sprite.rect.y = x1, y1

all_sprites.add(sprite)
all_sprites.draw(window)

# обновление окна
pygame.display.flip()

# запуск окна
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
