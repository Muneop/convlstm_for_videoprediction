
import json
import os
import shutil
from matplotlib import pyplot as plt

data_path = "zosystem/03"
file_list = os.listdir(data_path)#crop_20140310.daily.mer.sst.tif

for i in sorted(file_list):
    print(i)



def list_files_subdir(destpath, ext):
    json_list = []
    for path, subdirs, files in os.walk(destpath):
        for filename in files:
            f = os.path.join(path, filename)
            if os.path.isfile(f):
                if filename.endswith(ext):
                    json_list.append(f)
    return json_list
