import os
import shutil
import csv
import sys


folders = ['docs', 'images', 'audio']
audio_format = [
    '.aif', '.cda ', '.mid ', '.midi', '.mp3',
    '.mpa', '.ogg', '.wav', '.wma', '.wpl'
]
image_format = [
    '.ai', '.bmp', '.gif', '.ico', '.jpeg',
    '.jpg', '.png', '.ps', '.psd', '.svg',
    '.tif', '.tiff'
]
docs_format = [
    '.doc', '.docx', '.odt', '.pdf',
    '.rtf', '.tex', '.txt', '.wpd'
]


def pathCreation():
    '''go from the current folder to"files"
    creating paths if are required
    (docfolder, imagefolder, audiofolder)
    '''

    if 'files' not in os.listdir():
        print("Folder not found")
        sys.exit()
        return None

    path_files = os.getcwd() + '\\files'
    paths = []

    for folder in folders:
        path_folder = path_files + f'\\{folder}'

        if not os.path.exists(path_folder):
            os.makedirs(path_folder)
        paths.append(path_folder)

    return paths + [path_files]


def reorganize():
    '''reorder the files in their own sub folders
    '''
    path_files = pathCreation()
    fInfo = []

    for file_name in os.listdir(path_files[3]):
        fName, fType = os.path.splitext(file_name)
        fpath = path_files[3] + "\\{}".format(file_name)
        fSize = os.path.getsize(fpath)

        if fType in docs_format:
            shutil.move(fpath, path_files[0])
            fInfo.append([fName, fType, fSize])

        elif fType in image_format:
            shutil.move(fpath, path_files[1])
            fInfo.append([fName, fType, fSize])

        elif fType in audio_format:
            shutil.move(fpath, path_files[2])
            fInfo.append([fName, fType, fSize])

    return fInfo


def csv_func(info_filelist):
    '''printing out files information and summarizes them
    in a csv which will be created if it doesn't exist
    '''

    with open('recap.csv', 'a+', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(csv_file)
        csv_file.read()

        for element in info_filelist:
            csv_writer.writerow(element)
        csv_file.close()


def main():
    fileInfo = reorganize()
    for info_list in fileInfo:
        print("name:%s  type:%s  size:%sB" % tuple(info_list))

    csv_func(fileInfo)


if __name__ == "__main__":
    main()
