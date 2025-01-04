from functions import *
from classes import RunningCharacter

character_size = (300, 400)

# взятие данных обьектов
window_size, left_block_coordinates, down_block_coordinates, \
    text_coordinates = get_coordinates()
character_spawn_coordinates = make_character_spawn_(character_size,
                                                    left_block_coordinates,
                                                    down_block_coordinates)

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
    RunningCharacter(all_sprites, character_spawn_coordinates)
    all_sprites.draw(window)

    pygame.display.flip()

    # добавление времени
    clock = pygame.time.Clock()
    fps = 10
    one_second = 1

    # время для прокачки
    run_time_in_seconds = 0
    level_up_times = [20, 50, 1000]
    i = int(get_progress()[2]) - 1
    level_up_time = level_up_times[i]

    # запуск игры
    track_speed = 82
    running = True
    while running:
        # значения движения персонажа
        character_stand = True
        character_run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_pressed():
                # движение персонажа
                character_stand = False
                character_run = True

                run_time_in_seconds += one_second / fps
                if run_time_in_seconds >= level_up_time:
                    # изменение прогресса ног
                    write_progress(get_progress(), legs_flag=True)
                    level_up_time = level_up_times[(i := i + 1)]

        # обновление игры
        window.blit(background_image, (0, 0))
        all_sprites.update(window_size, fps, track_speed,
                           character_run, character_stand)
        text_update(window, text_coordinates,
                    get_progress()[2], level_up_time, int(run_time_in_seconds))
        all_sprites.draw(window)

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
