import os
import shutil
from fnmatch import fnmatch
pattern1 = "*.otf"
pattern2 = "*.ttf"
for root, dirs, files in os.walk('D:\\fonts\\fonts'):  # replace the . with your starting directory
   for file in files:
      if fnmatch(file, pattern1) or fnmatch(file, pattern2):
          path_file = os.path.join(root,file)
          shutil.copy2(path_file,'D:\\fonts\\fontExt') # 