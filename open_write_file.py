__author__ = 'Tony'
import os

def print_file1(fname):
    """
    :param fname:  just open the file
    :return: content of file
    """
    f1 = open(fname, 'r')
    print(f1.read())
    os.path.isfile(fname)

def make_file2(fname):
    """
    :param fname: write lines into a new file after checking the file if it is not exist
    :return:
    """
    if os.path.isfile(fname):
        print('The file is exist')
    else:
        f2 = open(fname, 'w')
        f2.write('Mary\n')
        f2.write('Tommy\n')

def append_file3(fname, title):
    f3 = open(fname, 'r+')
    temp = f3.read()
    temp = title + '\n\n' + temp
    f3.seek(0)
    f3.write(temp)

if __name__ == '__main__':
    print_file1('C:\\11.txt')
    make_file2('C:\\Users\\tony\\Desktop\\22.txt')
    append_file3('C:\\Users\\tony\\Desktop\\22.txt', 'title is here')
