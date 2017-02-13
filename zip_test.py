import os
import zipfile


startdir = r'/home/zheng/Documents/Test'

os.chdir(startdir)
file_list = os.listdir(startdir)
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        filename_zip = filename + '.zip'
        f = zipfile.ZipFile(filename_zip, 'w', zipfile.ZIP_DEFLATED)
        f.write(os.path.join(dirpath, filename))
        f.close()
        os.remove(os.path.join(dirpath, filename))
