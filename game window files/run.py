import pygame

# надо окно подрезать
# взятие данных обьектов
with open("objects coordinates.txt", mode="r") as file:
    data = [l.split(";") for l in file.read().split("\n")]

size = width, height = list(map(int, data[0][2].split(",")))

# инициализация окна
pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Pump It Up💪💪💪")

# добавление фона
background_image = pygame.image.load('window.png')
window.blit(background_image, (0, 0))
pygame.display.flip()

# запуск окна
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
