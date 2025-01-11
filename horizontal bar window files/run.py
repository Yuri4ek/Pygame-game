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

    # атрибуты игры для прокачки персонажа
    score = 0
    level_up_times = [10, 30, 1000]
    i = int(get_progress()[2]) - 1
    level_up_time = level_up_times[i]
    count = 0
    down_flag = False

    # запуск игры
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and not down_flag:
                count += 1
                if count == 3:
                    score += 1
                if score >= level_up_time:
                    write_progress(get_progress(), arm_flag=True)
                    level_up_time = level_up_times[i := 1]

        # для опускания персонажа
        if count > 2 or down_flag:
            down_flag = True
            count -= 1
        if count == 0:
            down_flag = False

        # обновление игры
        window.blit(background_image, (0, 0))
        all_sprites.update()
        text_update(window, text_coordinates, get_progress()[0], level_up_time, score)
        all_sprites.draw(window)

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
