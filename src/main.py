import os
import numpy as np
import time
from ast import Constant
from itertools import count
from module import graph as g

#константы
SEPARATOR_CHAR =', '
PATH ="src/files/"
PATH_READ = PATH+"arr_read_"
TXT=".txt"

#Сортировка пузырьком
def bubble_sort(arr):
    '''
    Сортировка Пузырьком
    @param arr - сортируемый массив
    @return отсортированный массив
    '''
    N = len(arr)
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Cортировка слиянием
def merge_sort(arr): 
    '''Сортировка слиянием
    @param arr - сортируемый массив
    @return отсортированный массив
    '''
    if len(arr) > 1: 
        mid = len(arr)//2
        left = arr[:mid] 
        right = arr[mid:]
        merge_sort(left) 
        merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1
    return arr

#Превращение массива в строку
def array_to_string(array):
    '''
    Преобразование массива в строку
    @param arr - числовой массив
    @return строку
    '''
    s=""
    for number in array:
        s += str(number)+SEPARATOR_CHAR
    return s.rstrip(SEPARATOR_CHAR)# удаление последнего разделителя

#создание массива
def array_create(count,path):
    '''
    Создать файл с новым массивом(разделитель ', ')

    @param count - размер массива
    @param path - путь куда сохранить файл
    '''
    rand_array = np.random.randint(0,1000,count)
    s=array_to_string(rand_array)
    file_writer(path, s)
    return len(rand_array)

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
    file = open(filename,"r")
    array = file.read()
    array = array.split(SEPARATOR_CHAR)
    array = list(map(int, array)) 
    file.close()
    return array

#Получить время работы сортировки
def get_time( method_to_run,array):
    '''
    Получить полный путь до файла
    @param method_to_run - метод время работы которого засекаем
    @returns время нахождения в функции
    '''
    start_time = time.time()
    method_to_run(array)
    return (time.time() - start_time)

#макро-функция создания новых случайных массивов в файлах
def create(count_array):
    for count in count_array:
        print("Count:"+str(count)+"Fact:"+str(array_create(count, PATH_READ+str(count)+TXT)))

#макро-функция сортировок
def sort(count_array):
    count = len(count_array)
    bubble_time_array = [-1.0 for i in range(count)]
    merge_time_array =[-1.0 for i in range(count)]

    for i in range(count):
        COUNT =str(count_array[i])

        arr_bubble = file_reader(PATH_READ+COUNT+TXT) #получение массива из файла
        arr_merge =arr_bubble.copy()

        bubble_time_array[i] = get_time(bubble_sort, arr_bubble)
        merge_time_array[i] = get_time(merge_sort, arr_merge)

        file_writer(PATH + "arr_bubble_write_"+COUNT+TXT, array_to_string(arr_bubble))
        file_writer(PATH + "arr_merge_write_"+COUNT+TXT, array_to_string(arr_merge))

        print("Count: " + COUNT, end=' ')
        print("\tBubble Sort Time:" + str(bubble_time_array[i]), end=' ')
        print("\tMerge Sort Time:" + str(merge_time_array[i]))

    g.print(count_array,bubble_time_array,merge_time_array);

def main():
    count_array=[1000,2000,3000,4000,5000,6000]

    #create(count_array)
    sort(count_array)

#Точка входа в программу
if __name__ == "__main__":
   main()