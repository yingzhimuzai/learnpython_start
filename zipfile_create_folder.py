import zipfile
import os
def zip_folder(folderdir,folder2zip,zipname):
    length_of_base = len(folderdir)
    f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for (root, dirs, files) in os.walk(folder2zip):
        for filename in files:
            filename_with_path = os.path.join(root, filename)
            f.write(filename_with_path, filename_with_path[length_of_base:])
    f.close()

folderdir = r'e:/Test'

os.chdir(folderdir)
file_list = os.listdir(folderdir)

for folder in file_list:
    if (os.path.isdir(os.path.join(folderdir,folder))):
        zip_folder(folderdir,os.path.join(folderdir, folder),folder + '.zip')
