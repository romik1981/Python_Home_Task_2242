"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os

nested_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
main_dir = 'Belyakov_Roman_DZ_7'
head_folder = 'my_project_1'
new_head_folder = 'new_my_project'

for folder in nested_folders:
    dir_path = os.path.join(head_folder, folder)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(head_folder, 'уже существует')
        break

#shutil.rmtree(os.path.join(head_folder))  # Удаление основной папки и подпапок
#os.rename(head_folder, new_head_folder)  # Переименование папки
#os.rename(os.path.join(head_folder, nested_folders[0]), os.path.join(head_folder, 'new_settings'))
