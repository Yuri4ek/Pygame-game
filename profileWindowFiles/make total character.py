from PIL import Image
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = ['..', 'assets', 'images', 'character', 'masses_progress']

# берет координаты конечностей
coords_path = file_path.copy()
coords_path.append("limbs coordinates.txt")
coords_fullname = os.path.join(current_dir, *coords_path)
with open(coords_fullname, mode="r") as coords_file:
    coords = [coord.split(";") for coord in coords_file.read().split("\n")]

# берет уровни прогресса персонажа
with open("progress.txt", mode="r") as progress_file:
    specifications = [specification.split(":")[1]
                      for specification in progress_file.read().split("\n")]

# берет картинку базового персонажа
character_path = file_path.copy()
character_path.append("Basic_El_Primo.png")
character_fullname = os.path.join(current_dir, *character_path)
character_im = Image.open(character_fullname)

# добавляет руки, если они прокачены
if specifications[0] != 1:
    arm_path = file_path.copy()
    arm_path.append(f"arm{specifications[0]}.png")
    arm_fullname = os.path.join(current_dir, *arm_path)

    try:
        coord = x1, y1, x2, y2 = list(map(int, coords[0][1].split(",")))
        arm_im = Image.open(arm_fullname).crop(coord)

        character_im.paste(arm_im, (x1, y1))
    except Exception:
        pass

# добавляет пресс, если он прокачен
if specifications[1] != 1:
    press_path = file_path.copy()
    press_path.append(f"press{specifications[1]}.png")
    press_fullname = os.path.join(current_dir, *press_path)

    try:
        coord = x1, y1, x2, y2 = list(map(int, coords[1][1].split(",")))
        press_im = Image.open(press_fullname).crop(coord)

        character_im.paste(press_im, (x1, y1))
    except Exception:
        pass

# добавляет ноги, если они прокачены
if specifications[2] != 1:
    legs_path = file_path.copy()
    legs_path.append(f"legs{specifications[2]}.png")
    legs_fullname = os.path.join(current_dir, *legs_path)

    try:
        coord = x1, y1, x2, y2 = list(map(int, coords[2][1].split(",")))
        legs_im = Image.open(legs_fullname).crop(coord)

        character_im.paste(legs_im, (x1, y1))
    except Exception:
        pass

character_im.save("total_character.png")