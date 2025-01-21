import pygame
import os


def get_path(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'mainWindowFiles', name]
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def get_coordinates():
    # взятие данных обьектов
    with open(get_path("objects coordinates.txt"), mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    start_game_btn_coordinates = list(map(int, data[1][1].split(",")))
    settings_btn_coordinates = list(map(int, data[2][1].split(",")))

    return (size, start_game_btn_coordinates, settings_btn_coordinates)


def btn_click(mouse_coordinates, btn_coordinates):
    m_x, m_y = mouse_coordinates
    b_x1, b_y1, b_x2, b_y2 = btn_coordinates
    return b_x1 <= m_x <= b_x2 and b_y1 <= m_y <= b_y2


def run_window(window_size, start_game_btn_coordinates,
               settings_btn_coordinates):
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

    # флаги для запуска других окон
    game_flag = False
    settings_flag = False

    # добавление фона
    background_image = pygame.image.load(get_path('window.png'))
    window.blit(background_image, (0, 0))
    pygame.display.flip()

    # запуск окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_coordinates = event.pos
                # нажата ли кнопка игры
                if btn_click(mouse_coordinates, start_game_btn_coordinates):
                    game_flag = True
                    running = False
                # нажата ли кнопка настроек
                elif btn_click(mouse_coordinates,
                                  settings_btn_coordinates):
                    settings_flag = True
                    running = False

    return game_flag, settings_flag
