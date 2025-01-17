from functions import *

# взятие данных обьектов
size, creators_txt_coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Pump It Up💪💪💪")

    run_window(window)

    pygame.quit()
