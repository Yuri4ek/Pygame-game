import pygame
import mainWindowFiles.functions as mainWindow
import gameWindowFiles.functions as gameWindow
import settingsWindowFiles.functions as settingsWindow

if __name__ == "__main__":
    # инициализация pygame
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Pump It Up💪💪💪")

    # запуск начального меню
    game_flag, settings_flag = mainWindow.run_window(
        *mainWindow.get_coordinates())

    # запуск игры
    if game_flag:
        hands_flag, legs_flag, press_flag = gameWindow.run_window(
            *gameWindow.get_coordinates())
    # запуск меню настроек
    if settings_flag:
        settingsWindow.run_window(*settingsWindow.get_coordinates())

    pygame.quit()
