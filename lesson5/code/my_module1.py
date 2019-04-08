# 1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
# Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os


def make_dir():
    i=1
    while i<10:
        if os.path.exists(os.path.join(os.getcwd(),'dir_'+str(i))):
            print("Директория dir_{} существует".format(str(i)))
        else:
            # new_path = os.path.join(os.getcwd(), str(i))
            os.mkdir(os.path.join(os.getcwd(),'dir_'+str(i)))
        i+=1

def remove_dir():
    i=1
    while i<10:
        if os.path.exists(os.path.join(os.getcwd(), 'dir_' + str(i))):
            os.rmdir(os.path.join(os.getcwd(),'dir_'+str(i)))
        else:
            print("Директория dir_{} не существует".format(str(i)))
        i+=1

#make_dir()
#remove_dir()