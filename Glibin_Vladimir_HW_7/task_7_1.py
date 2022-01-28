import os

path = r'C:\Users\vglibin\PycharmProjects\Python\Glibin_Vladimir_HW_7'
proj_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


full_path = os.path.join(path, proj_name)
create_folder(full_path)

for f in folders:
    folder = os.path.join(full_path, f)
    create_folder(folder)
