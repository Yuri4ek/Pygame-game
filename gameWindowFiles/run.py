from functions import *

# надо окно подрезать
# взятие данных обьектов
coordinates = get_coordinates()

if __name__ == "__main__":
    # инициализация окна
    pygame.init()
    pygame.display.set_caption("Pump It Up💪💪💪")

    hands_flag, legs_flag, press_flag = run_window(*coordinates)

    pygame.quit()
