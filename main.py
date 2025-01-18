from mainWindowFiles.functions import *

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pump It Up💪💪💪")
run_window(*get_coordinates())
pygame.quit()