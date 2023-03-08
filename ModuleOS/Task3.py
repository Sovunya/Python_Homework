"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""

import os

target_dir = r'D:\target'

if os.path.exists(target_dir):
    for folder in os.listdir(target_dir):
        folder_path = os.path.join(target_dir, folder)
        if os.path.isdir(folder_path):
            folder_num = int(folder)
            if folder_num % 2 == 0:
                new_name = f"folder_{folder_num}"
                new_folder_path = os.path.join(target_dir, new_name)
                os.rename(folder_path, new_folder_path)

