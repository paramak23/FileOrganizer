#This code is mainly used to organize the random files into organized and moved to concern directory
#For example, if you have "pdf" file, which will be moved to corresponding "pdf" directory, which automatically created
#It will not touch the files already existed folders
#the following python code will be done,
#step 1 ------> identify the files in a directory
#step 2 ------> create the new directory in the name of file extension into the directory
#step 3 ------> move the files to newly created directory

#This will be done automatically, the source required will be the concern directory path.... 

import os
import json
import shutil

root_directory = input('Please input the link: ')
file_list = os.listdir(root_directory)
ext_list = []
for i in range(len(file_list)):
    if os.path.isfile(os.path.join(root_directory, file_list[i])):
        file_text = file_list[i].split('.')
        file_ext = file_text[-1].strip()
        ext_list.append(file_ext)
new_ext_list = list(set(ext_list))
new_ext_list.sort()
#print(new_ext_list)

#Creating the directory in the name of extension created already
try:
    
    for i in range(len(new_ext_list)):
        new_dir_path = os.path.join(root_directory, new_ext_list[i])
        created_new_dir = os.mkdir(new_dir_path)

except FileExistsError:
    pass

#moving the files to corresponding new directory
for dirpath, dirnames, files in os.walk(os.path.join(root_directory)):
    if isinstance(files, list):
        for each_file in files:
            if os.path.isfile(os.path.join(dirpath, each_file)):
                src = os.path.join(dirpath, each_file)
            
            if isinstance(dirnames, list):
                for each_dir in dirnames:
                    if each_dir in each_file:
#                        print(f'{each_dir} has in the {each_file}')
                        dst = os.path.join(root_directory, each_dir)
                        shutil.move(src = src, dst = dst)
                        print(f'{each_file} is moved to {each_dir}')

