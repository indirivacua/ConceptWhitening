import os
import shutil
import zipfile

# Descomprime el archivo val_256.zip
with zipfile.ZipFile('val_256.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Crea un diccionario para mapear los índices de clase a nombres de clase
class_dict = {}
with open('categories_places365.txt', 'r') as f:
    for line in f:
        class_name, class_index = line.strip().split()
        class_dict[int(class_index)] = class_name.split('/')[2]

# Crea las carpetas para cada clase
if not os.path.exists('val'):
    os.mkdir('val')
for class_name in class_dict.values():
    if not os.path.exists(os.path.join('val', class_name)):
        os.mkdir(os.path.join('val', class_name))

# Mueve las imágenes a sus respectivas carpetas de clase
with open('places365_val.txt', 'r') as f:
    for line in f:
        image_name, class_index = line.strip().split()
        class_index = int(class_index)
        class_name = class_dict[class_index]
        src_path = os.path.join('val_256', image_name)
        dst_path = os.path.join('val', class_name, image_name)
        shutil.move(src_path, dst_path)
