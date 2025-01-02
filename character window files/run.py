from functions import *

# координаты окна и его объектов
size, character_view_coordinates, \
    general_lvl_coordinates, other_lvl_coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Pump It Up💪💪💪")

    # добавление фона
    background_image = pygame.image.load('window.png')
    window.blit(background_image, (0, 0))

    # вывод персонажа
    all_sprites = pygame.sprite.Group()
    display_character(all_sprites, character_view_coordinates)
    all_sprites.draw(window)

    # вывод уровней персонажа
    display_character_progress(window,
                               general_lvl_coordinates, other_lvl_coordinates)

    # обновление окна
    pygame.display.flip()

    # запуск окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
