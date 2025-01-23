from functions import *

window_style = "gym"

# взятие данных обьектов
coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    pygame.display.set_caption("Pump It Up💪💪💪")

    game_flag, settings_flag, profile_flag = run_window(window_style,
                                                        *coordinates)

    pygame.quit()
