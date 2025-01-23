import os
import pygame


def get_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def clear_progress(file_path):
    file_name = get_path(file_path)
    with open(file_name, mode="w") as progress_file:
        progress_file.write("arm:1\npress:1\nlegs:1")


def start_screen(window):
    image_path = ["assets", "images", "backgrounds", "start.png"]
    background = pygame.image.load(get_path(image_path))
    window.blit(background, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
