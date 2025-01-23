import os


def get_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def clear_progress(file_path):
    file_name = get_path(file_path)
    with open(file_name, mode="w") as progress_file:
        progress_file.write("arm:1\npress:1\nlegs:1")
