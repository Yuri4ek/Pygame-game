import pygame
from functions import load_image

# взятие данных обьектов
with open("objects coordinates.txt", mode="r") as file:
    data = [l.split(";") for l in file.read().split("\n")]
character_view = x1, y1, x2, y2 = list(map(int,
                                           data[1][1].split(",")
                                           )
                                       )
print(character_view)

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
sprite.image = load_image("test files",
                          "El_Primo.png",
                          character_view)
sprite.rect = sprite.image.get_rect()
sprite.rect.x, sprite.rect.y = x1, y1

all_sprites.add(sprite)
all_sprites.draw(window)

pygame.display.flip()

# запуск окна
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
