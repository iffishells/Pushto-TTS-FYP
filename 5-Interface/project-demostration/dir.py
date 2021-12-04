import os

speech_db = {}
folder = 'Datasets'

folder_list = []
for name in os.listdir(folder):
    if os.path.isdir(os.path.join(folder,name)):
        folder_list.append(name)

# print(folder_list)

# for sub_dir_name in folder_list:
    # print(sub_dir_name)
!ls