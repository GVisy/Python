import os
import shutil

proj_dir = 'my_project'
templates_dir = 'templates'

root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), proj_dir)
template = os.path.join(root_dir, templates_dir)

for root, dirs, files in os.walk(root_dir):
    for d in dirs:
        if d == 'templates':
            path = os.path.join(root, d)
            shutil.copytree(path, templates_dir, dirs_exist_ok=True)
