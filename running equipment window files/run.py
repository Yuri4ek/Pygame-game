from functions import *
from classes import RunningCharacter

# взятие данных обьектов
window_size, character_spawn_coordinates, \
    left_block_coordinates, down_block_coordinates = get_coordinates()

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
    fps = 30

    # запуск игры
    track_speed = 82
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # движение персонажа
        window.blit(background_image, (0, 0))
        all_sprites.update(window_size, fps, track_speed)
        all_sprites.draw(window)
        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
