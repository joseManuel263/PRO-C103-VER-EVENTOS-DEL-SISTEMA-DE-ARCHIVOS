from distutils import extension
from importlib.resources import path
import os
import shutil

import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print("\n\nPRO-C103: VER EVENTOS DEL SISTEMA DE ARCHIVOS\n\n〔ఠﭛ ఠ〕👍\n\nNote: VSC acepta rutas con “ / “.\n\n")

from_dir = input("¿Cual es La ruta de origen?: ")
to_dir = input("¿Cual es La ruta de destino?: ")

list_of_files = os.listdir(from_dir)
#print("\n\n"+list_of_files)

for file_name in list_of_files:
    name, extension = os.splitext(file_name)
    print("Name: "+name)
    print("Extension: "+extension)
    print("\n")
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', 'pdf']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+"Archivos_Documentos"
        path3 = to_dir+'/'+"Archivos_Documentos"+file_name
        if os.path.exists(path2):
            print("Moviendo: "+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moviendo: "+file_name+"...")
            shutil.move(path1,path3)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"\n¡Oye, {event.src_path} ha sido creado!\n⸦(⏓ᗨ⏓)⸧\n\n")
        time.sleep(1)
    def on_modified(self, event):
        print(f"\nEl archivo o directorio se modifico\n(╯~ ̫ ^)╯\n\n")
        time.sleep(1)
    def on_moved(self, event):
        print(f"\nEl archivo o directorio se movio o cambio de nombre\n\〈ᵔڡ ᵔ〉/\n\n")
        time.sleep(1)
    def on_deleted(self, event):
        print(f"\n¡Lo siento! ¡Alguien borró {event.src_path}!\n¯\_(ఠ‸ఠ)_/¯\n\n")
        time.sleep(1)

# Inicia la clase event handler
event_handler = FileEventHandler()

# Inicia Observer
observer = Observer()

# Programa Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicia Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()