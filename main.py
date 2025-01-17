from mainWindowFiles.functions import *

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pump It Up💪💪💪")
run_window(*get_coordinates())
pygame.quit()