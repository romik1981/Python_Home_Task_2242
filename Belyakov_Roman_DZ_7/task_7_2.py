"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
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
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import yaml
import os

d = {'my_project':
    [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py',
            {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]
        },
        {'authapp': ['__init__.py', 'models.py', 'views.py',
                    {'templates': [{
                         'authapp': ['base.html', 'index.html']}]
                    }]
        }
    ]
}

f = open('config.yaml', 'w')
f.write(yaml.dump(d))
f.close()

with open("config.yaml") as y_file:
    d = yaml.safe_load(y_file)


def create_data(data):
    for folder, data_tmps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in data_tmps:
            if isinstance(data_tmp, dict):
                create_data(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')


create_data(d)
