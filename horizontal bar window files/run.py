from functions import *

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
    pass

    # добавление текста
    text_update(window, text_coordinates, get_progress()[0], 0, 0)

    pygame.display.flip()

    # запуск игры
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
