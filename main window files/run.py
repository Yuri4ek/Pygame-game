from functions import *

# взятие данных обьектов
size, start_game_btn_coordinates, settings_btn_coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Pump It Up💪💪💪")

    game_flag, settings_flag = run_window(window, start_game_btn_coordinates,
                                          settings_btn_coordinates)

    pygame.quit()
