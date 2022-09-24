import os
from main import SEPARATOR_CHAR 
#получение полного пути файла
def file_get_full_path(filename):
    '''
    Получить полный путь до файла
    @param filename - наименование файла
    @returns путь до файла с заданным наименованием
    '''
    file_dir = os.path.abspath(os.path.dirname(__file__))
    file_to_save = os.path.join(file_dir, '..', filename)
    return file_to_save

#запись в файл
def file_writer(filename, save_string):
    '''
    Запись в файл
    @param filename - имя файла
    @param row_array - массив данных строки таблицы
    '''
    file_name_to_save = file_get_full_path(filename)
    with open(file_name_to_save,'a',encoding = 'utf-8') as resultFile:
        resultFile.write(save_string)

#Чтение из файла
def file_reader(filename):
    '''
    Чтение из файла
    @param filename - имя файла
    '''
    file_name_to_read = file_get_full_path(filename)
    file = open(file_name_to_read,"r")
    array = file.read()
    array = array.split(SEPARATOR_CHAR)
    array = list(map(int, array)) 
    file.close()
    return array