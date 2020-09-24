import exiftool
import os
import zipfile

def version(f, v):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(f)
        try:
            if metadata['XMP:Version'] == 1.1:
                print(f)
        except:
                pass

def check_password(f):
    try:
        with open(f, 'r') as reader:
            data = reader.read()
            if 'password' in data:
                print('Password is in: ' + f)
    except:
        pass

file_number = 0
with zipfile.ZipFile('final-final-compressed.zip', 'r') as zip_ref:
    zip_ref.extractall('final-final-uncompressed')

    os.chdir('final-final-uncompressed')
    for subdir, dirs, zips in os.walk('./'):
        for z in zips:
            with zipfile.ZipFile(z, 'r') as zi:
                zi.extractall(z[:-4])
                os.chdir(z[:-4])

                for subdir, dirs, files in os.walk('./'):
                    for f in files:
                        file_number += 1
                        check_password(f)
                        version(f, 1.1)


                os.chdir('../')

    print("Number of files: " + str(file_number))
