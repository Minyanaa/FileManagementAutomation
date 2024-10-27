import os
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import splitext, exists

source_dir = r"C:\Users\User\Documents\Personal\Python\Basic\Downloads"
dest_dir_img = r"C:\Users\User\Documents\Personal\Python\Basic\Downloads\Downloaded_Images"
dest_dir_video = r"C:\Users\User\Documents\Personal\Python\Basic\Downloads\Downloaded_Videos"
dest_dir_files = r"C:\Users\User\Documents\Personal\Python\Basic\Downloads\Downloaded_Files"

def checkUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # Si el archivo existe, se añade un número al final del archivo
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move(dest, entry, name):
    if entry.is_file():  # Solo mover si es un archivo
        file_exists = os.path.exists(dest + "/" + name)
        if file_exists:
            name = checkUnique(dest, name)
        # Añadimos un intento de mover el archivo con un retardo en caso de fallo
        attempts = 3
        for _ in range(attempts):
            try:
                shutil.move(entry.path, os.path.join(dest, name))
                break
            except PermissionError:
                time.sleep(1)  # Espera 1 segundo antes de reintentar
                continue

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():  # Asegúrate de que solo se procese si es un archivo
                    name = entry.name
                    if name.endswith(('.png', '.jpeg', '.jpg')):
                        dest = dest_dir_img
                        move(dest, entry, name)
                    elif name.endswith(('.mov', '.mp4')):
                        dest = dest_dir_video  # Cambiado a la carpeta correcta
                        move(dest, entry, name)
                    else:
                        dest = dest_dir_files
                        move(dest, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
