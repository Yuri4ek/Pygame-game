from functions import *
from classes import Character

# взятие данных обьектов
size, character_spawn_coordinates, \
    left_block_coordinates, down_block_coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Pump It Up💪💪💪")

    # добавление фона
    background_image = pygame.image.load('window.png')
    window.blit(background_image, (0, 0))

    # добавление персонажа
    all_sprites = pygame.sprite.Group()
    Character(all_sprites, character_spawn_coordinates)
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
