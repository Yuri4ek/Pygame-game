import pygame
import os


def get_path(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'gameWindowFiles', name]
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def get_coordinates():
    '''
        Возвращает координаты окна и его обьектов
    '''

    # взятие данных обьектов
    with open(get_path("objects coordinates.txt"), mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    simulator_hands_coordinates = list(map(int, data[1][1].split(",")))
    simulator_legs_coordinates = list(map(int, data[2][1].split(",")))
    simulator_press_coordinates = list(map(int, data[3][1].split(",")))
    dividing_line_coordinates = list(map(int, data[4][1].split(",")))
    player_profile_coordinates = list(map(int, data[5][1].split(",")))
    player_inventory_coordinates = list(map(int, data[6][1].split(",")))

    return (size, simulator_hands_coordinates, simulator_legs_coordinates,
            simulator_press_coordinates, dividing_line_coordinates,
            player_profile_coordinates, player_inventory_coordinates)


def run_window(size, simulator_hands_coordinates, simulator_legs_coordinates,
               simulator_press_coordinates, dividing_line_coordinates,
               player_profile_coordinates, player_inventory_coordinates):
    window = pygame.display.set_mode(size)

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
