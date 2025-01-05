def get_coordinates():
    '''
        Возвращает координаты окна и его обьектов
    '''

    # взятие данных обьектов
    with open("objects coordinates.txt", mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    text_coordinates = list(map(int, data[1][1].split(",")))
    upper_kernel_coordinates = list(map(int, data[2][1].split(",")))
    left_kernel_coordinates = list(map(int, data[3][1].split(",")))
    right_kernel_coordinates = list(map(int, data[4][1].split(",")))

    return (size, text_coordinates, upper_kernel_coordinates,
            left_kernel_coordinates, right_kernel_coordinates)
