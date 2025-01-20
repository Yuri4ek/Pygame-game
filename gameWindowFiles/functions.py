import pygame
import os
from classes import MainCharacter


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
    character_spawn_coordinates = list(map(int, data[4][1].split(",")))
    dividing_line_coordinates = list(map(int, data[5][1].split(",")))
    player_profile_coordinates = list(map(int, data[6][1].split(",")))
    player_inventory_coordinates = list(map(int, data[7][1].split(",")))

    return (size, simulator_hands_coordinates, simulator_legs_coordinates,
            simulator_press_coordinates, character_spawn_coordinates,
            dividing_line_coordinates, player_profile_coordinates,
            player_inventory_coordinates)


def check_touch(character_coordinates, object_coordinates):
    x1, y1, x2, y2 = object_coordinates
    return x1 <= character_coordinates[0] <= x2 and \
        y1 <= character_coordinates[1] <= y2


def run_window(size, simulator_hands_coordinates, simulator_legs_coordinates,
               simulator_press_coordinates, character_spawn_coordinates,
               dividing_line_coordinates, player_profile_coordinates,
               player_inventory_coordinates):
    window = pygame.display.set_mode(size)

    # флаги для запуска тренажеров
    hands_flag = False
    legs_flag = False
    press_flag = False

    # добавление фона
    background_image = pygame.image.load(get_path('window.png'))
    window.blit(background_image, (0, 0))

    # добавление персонажа
    all_sprites = pygame.sprite.Group()
    character = MainCharacter(all_sprites, character_spawn_coordinates)
    all_sprites.draw(window)

    pygame.display.flip()

    # добавление времени
    clock = pygame.time.Clock()
    fps = 60

    # запуск окна
    running = True
    while running:
        step_x = 0
        step_y = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                step_x = -1
            if keys[pygame.K_RIGHT]:
                step_x = 1
            if keys[pygame.K_UP]:
                step_y = -1
            if keys[pygame.K_DOWN]:
                step_y = 1

        window.blit(background_image, (0, 0))
        all_sprites.update(step_x, step_y)
        all_sprites.draw(window)

        clock.tick(fps)
        pygame.display.flip()

        # проверка на заход в тренажеры
        character_coordinates = character.rect.x, character.rect.y
        if check_touch(character_coordinates, simulator_hands_coordinates):
            hands_flag = True
            running = False
        elif check_touch(character_coordinates, simulator_legs_coordinates):
            legs_flag = True
            running = False
        elif check_touch(character_coordinates, simulator_press_coordinates):
            press_flag = True
            running = False

    return hands_flag, legs_flag, press_flag
