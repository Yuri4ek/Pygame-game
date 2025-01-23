import pygame
import os
from pullUpWindowFiles.classes import PullingCharacter


def get_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def get_progress():
    '''
        Возвращает прогресс персонажа
    '''
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
    '''
        Записывает новые значения в progress.txt
    '''
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
    with open(get_path(["..", "pullUpWindowFiles", "objects coordinates.txt"]),
              mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    text_coordinates = list(map(int, data[1][1].split(",")))
    character_coordinates = list(map(int, data[2][1].split(",")))

    return (size, text_coordinates, character_coordinates)


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
               character_coordinates):
    window = pygame.display.set_mode(window_size)

    # добавление фона
    background_path = ["..", "assets", "images", "backgrounds",
                       f"pullUp_{window_style}.png"]
    background_image = pygame.image.load(get_path(background_path))
    window.blit(background_image, (0, 0))
    pygame.display.flip()

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
    count = 1
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
        if down_flag:
            count -= 1
        if count > 2:
            down_flag = True
        if count == 0:
            down_flag = False

        # обновление игры
        window.blit(background_image, (0, 0))
        all_sprites.update(count)
        text_update(window, text_coordinates, get_progress()[0], level_up_time,
                    score)
        all_sprites.draw(window)

        clock.tick(fps)
        pygame.display.flip()
