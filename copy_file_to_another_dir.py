import shutil
import os

# path to source directory
src_dir = 'D:\fonts\fonts'

# path to destination directory
dest_dir = 'C:\\Users\\CEEWHY\\Downloads\\aopy'

# getting all the files in the source directory
files = os.listdir(src_dir)

shutil.copytree(src_dir, dest_dir)
