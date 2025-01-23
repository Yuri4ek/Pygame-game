import os
import pygame
from runWindowFiles.classes import RunningCharacter


def get_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def get_progress():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'profileWindowFiles', 'progress.txt']
    progress_file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(progress_file_name):
        return None

    # берет уровни прогресса персонажа
    with open(progress_file_name, mode="r") as progress_file:
        specifications = [specification.split(":")[1]
                          for specification in
                          progress_file.read().split("\n")]

    return specifications


def write_progress(specifications,
                   arm_flag=False, press_flag=False, legs_flag=False):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'profileWindowFiles', 'progress.txt']
    progress_file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(progress_file_name):
        return None

    # прогресс персонажа
    specifications[0] = str(int(specifications[0]) + 1) \
        if arm_flag and int(specifications[0]) < 3 else specifications[0]

    specifications[1] = str(int(specifications[1]) + 1) \
        if press_flag and int(specifications[1]) < 3 else specifications[1]

    specifications[2] = str(int(specifications[2]) + 1) \
        if legs_flag and int(specifications[2]) < 3 else specifications[2]

    progress_text = f"arm:{specifications[0]}\n" \
                    f"press:{specifications[1]}\n" \
                    f"legs:{specifications[2]}"

    # записывает прогресс
    with open(progress_file_name, mode="w") as progress_file:
        progress_file.write(progress_text)


def get_coordinates():
    # взятие данных обьектов
    with open(get_path(["..", "runWindowFiles", "objects coordinates.txt"]),
              mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    left_block_coordinates = list(map(int, data[1][1].split(",")))
    down_block_coordinates = list(map(int, data[2][1].split(",")))
    text_coordinates = list(map(int, data[3][1].split(",")))

    return (size, left_block_coordinates, down_block_coordinates,
            text_coordinates)


def get_total_coordinates():
    character_size = (300, 400)

    window_size, left_block_coordinates, down_block_coordinates, \
        text_coordinates = get_coordinates()
    character_spawn_coordinates = make_character_spawn(character_size,
                                                       left_block_coordinates,
                                                       down_block_coordinates)

    return window_size, text_coordinates, character_spawn_coordinates


def make_character_spawn(character_size,
                         left_block_coordinates, down_block_coordinates):
    w, h = character_size

    x1 = left_block_coordinates[2]
    y1 = down_block_coordinates[1] - h
    x2 = x1 + w
    y2 = y1 + h

    return (x1, y1, x2, y2)


def text_update(window, text_coordinates, character_level, purpose, score):
    x1, y1, x2, y2 = text_coordinates
    text_size = 60
    font = pygame.font.Font(None, text_size)
    color = pygame.Color(0, 0, 0)

    level_text = font.render(f"Уровень {character_level}", True, color)
    window.blit(level_text, (x1, y1))

    purpose_text = font.render(f"Цель {purpose}", True, color)
    window.blit(purpose_text, (x1, y1 + 10 + text_size))

    score_text = font.render(f"Очки {score}", True, color)
    window.blit(score_text, (x1, y1 + 10 * 2 + text_size * 2))


def run_window(window_style, window_size, text_coordinates,
               character_spawn_coordinates):
    window = pygame.display.set_mode(window_size)

    # добавление фона
    background_path = ["..", "assets", "images", "backgrounds",
                       f"run_{window_style}.png"]
    background_image = pygame.image.load(get_path(background_path))
    window.blit(background_image, (0, 0))

    # добавление персонажа
    all_sprites = pygame.sprite.Group()
    RunningCharacter(all_sprites, character_spawn_coordinates)
    all_sprites.draw(window)

    pygame.display.flip()

    # добавление времени
    clock = pygame.time.Clock()
    fps = 8
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
