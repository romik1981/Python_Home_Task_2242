"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
"""

import os
import shutil


head_folder = 'my_project'


folder_temp = os.listdir(head_folder)

try:
    for item in folder_temp:
        if os.path.exists(os.path.join(head_folder, item, 'templates')):
            temp = os.listdir(os.path.join(head_folder, item, 'templates'))
            shutil.copytree(os.path.join(head_folder, item, 'templates', temp[0]),
                            os.path.join(head_folder, 'templates', temp[0]))
except FileExistsError:
    print('Директории уже созданы: ', os.path.join(head_folder, 'templates'))
finally:
    print('end')
