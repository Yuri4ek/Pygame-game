from functions import *
from classes import PullingCharacter

character_size = (300, 450)

# взятие данных обьектов
window_size, text_coordinates, character_coordinates, \
    upper_kernel_coordinates, left_kernel_coordinates, \
    right_kernel_coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Pump It Up💪💪💪")

    # добавление фона
    background_image = pygame.image.load('window.png')
    window.blit(background_image, (0, 0))

    # добавление персонажа
    all_sprites = pygame.sprite.Group()
    PullingCharacter(all_sprites, character_coordinates)
    all_sprites.draw(window)

    # добавление текста
    text_update(window, text_coordinates, get_progress()[0], 0, 0)

    pygame.display.flip()

    # добавление времени
    clock = pygame.time.Clock()
    fps = 3

    # запуск игры
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # обновление игры
        window.blit(background_image, (0, 0))
        all_sprites.update()
        text_update(window, text_coordinates, get_progress()[0], 0, 0)
        all_sprites.draw(window)

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
