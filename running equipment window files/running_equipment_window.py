import pygame
from functions import load_image
import os

# взятие данных обьектов
with open("objects coordinates.txt", mode="r") as file:
    data = [l.split(";") for l in file.read().split("\n")]
character_spawn_coordinates = x1, y1, x2, y2 = list(map(int,
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

# добавление персонажа
all_sprites = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = ('..', 'assets', 'images', 'character', 'Running_El_Primo.png')
sprite.image = load_image(current_dir, file_path, character_spawn_coordinates)

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
