import zipfile
import os
def extract_zipfile(zipdir,folderdir):
    f = zipfile.ZipFile(zipname, 'r')
    for filename in f.namelist():
        f.extract(filename,zipdir)
    f.close()

zipdir = r'e:/Test'

os.chdir(zipdir)
zip_list = os.listdir(zipdir)

for zipname in zip_list:
    if os.path.splitext(zipname)[1] == '.zip':
        extract_zipfile(zipdir,zipdir)
