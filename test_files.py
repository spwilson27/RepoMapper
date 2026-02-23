import sys, os
from repomap_server import find_src_files

files = find_src_files(os.path.abspath('../..'))
print("LEN FILES:", len(files))
for i in range(5):
    if i < len(files):
        print(files[i])
