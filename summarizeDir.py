import os
from os import walk


def summarizeDirectory(p):

    #check if directory size > 0
    if os.path.getsize(p) == 0:
        raise ValueError("AN empty directory!!!")

    with open("dirInfo.txt","a")as fp:
        fp.write(f"directory name : {os.path.splitext(p)[0]}\n")
        fp.write(f"directory size : {os.path.getsize(p)}\n")
        fp.write((f'num of file : {get_num_of_file(p)}\n'))
        numOfSub = get_num_of_subDir(p)
        fp.write((f'num of sub directory : {numOfSub}\n'))
        if numOfSub != 0 :
            fp.write((f'sub directory info :\n'))

    # print sub directory information
    filenames = os.listdir(p)
    for name in filenames:
        name = f'{p}\\{name}'
        if os.path.isdir(name):
            summarizeDirectory(name)


def get_num_of_file(path):
    count = 0
    filenames = get_list_dir(path)
    for name in filenames :
        name = f'{path}\\{name}'
        if os.path.isfile(name):
            count+=1
    return count

def get_num_of_subDir(path):
    count = 0
    filenames = get_list_dir(path)
    for name in filenames :
        name = f'{path}\\{name}'
        if os.path.isdir(name):
            count+=1
    return count

def get_list_dir(path):
    filenames = os.listdir(path)
    return filenames
