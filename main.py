import pygame
import mainWindowFiles.functions as mainWindow
import gameWindowFiles.functions as gameWindow
import settingsWindowFiles.functions as settingsWindow
import profileWindowFiles.functions as profileWindow
import runWindowFiles.functions as runWindow
import pullUpWindowFiles.functions as pullUpWindow

window_style = "gym"

if __name__ == "__main__":
    # инициализация pygame
    pygame.init()
    window = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Pump It Up💪💪💪")

    # запуск начального меню
    game_flag, settings_flag, profile_flag = mainWindow.run_window(
        window_style, *mainWindow.get_coordinates())

    # запуск игры
    if game_flag:
        hands_flag, legs_flag, press_flag = gameWindow.run_window(
            window_style, *gameWindow.get_coordinates())

        if hands_flag:
            pullUpWindow.run_window(window_style,
                                    *pullUpWindow.get_coordinates())
        if legs_flag:
            runWindow.run_window(window_style,
                                 *runWindow.get_total_coordinates())
        if press_flag:
            print("Недоступно в вашем регионе")
    # запуск меню настроек
    if settings_flag:
        settingsWindow.run_window(window_style,
                                  *settingsWindow.get_coordinates())
    # запуск профиля игрока
    if profile_flag:
        profileWindow.run_window(window_style,
                                 *profileWindow.get_coordinates())

    pygame.quit()
