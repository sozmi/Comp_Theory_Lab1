import numpy as np
import time
import modules.graph as g
import modules.sort as s
import modules.file_manager as fm

#константы
SEPARATOR_CHAR =', '
PATH ="../files/"
PATH_READ = PATH+"arr_read_"
TXT=".txt"

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
    fm.file_writer(path, s)
    return len(rand_array)

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

        arr_bubble = fm.file_reader(PATH_READ+COUNT+TXT) #получение массива из файла
        arr_merge =arr_bubble.copy()

        bubble_time_array[i] = get_time(s.bubble_sort, arr_bubble)
        merge_time_array[i] = get_time(s.merge_sort, arr_merge)

        fm.file_writer(PATH + "arr_bubble_write_"+COUNT+TXT, array_to_string(arr_bubble))
        fm.file_writer(PATH + "arr_merge_write_"+COUNT+TXT, array_to_string(arr_merge))

        print("Count: " + COUNT, end=' ')
        print("\tBubble Sort Time:" + str(bubble_time_array[i]), end=' ')
        print("\tMerge Sort Time:" + str(merge_time_array[i]))

    g.print(count_array, bubble_time_array,merge_time_array)

def main():
    COUNT_ARRAY=[1000,2000,3000,4000,5000,6000]

    #create(COUNT_ARRAY)
    sort(COUNT_ARRAY)

#Точка входа в программу
if __name__ == "__main__":
   main()