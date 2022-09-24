# Полностью автоматическое создание трендов с matplotlib
import matplotlib.pyplot as plt # импортируем построитель графиков из библиотеки matplotlib
import numpy as np # импортируем библиотеку numpy для работы с массивами numpy
from sklearn.metrics import r2_score # функция для расчёта критерия r^2

def print(x,y1,y2):

    # Массивы numpy по входным данным
    numpy_y1 = np.array(y1)
    numpy_y2 = np.array(y2)
    numpy_x = np.array(x)

    # Линии тренда
    # линейный (автоматическое создание)
    set_line_by_data1 = np.polyfit(numpy_x, numpy_y1, 6) # полином первой степени
    linear_trend1 = np.poly1d(set_line_by_data1) # снижение размерности до одномерного массива
    set_line_by_data2 = np.polyfit(numpy_x, numpy_y2, 1) # полином первой степени
    linear_trend2 = np.poly1d(set_line_by_data2) # снижение размерности до одномерного массива


    # Отображение графиков
    plt.figure(figsize=(10, 10)) # размер графика
    plt.subplot(1, 1, 1)

    plt.scatter(numpy_x, numpy_y1, label = 'bubble') # точечный график по x_numpy, y_numpy
    plt.plot(numpy_x, linear_trend1(numpy_x), linestyle='dashed', color="blue", label = 'polynom trend')

    plt.scatter(numpy_x, numpy_y2, label = 'merge') # точечный график по x_numpy, y_numpy
    plt.plot(numpy_x, linear_trend2(numpy_x), linestyle='dashed', color="red", label = 'linear trend') 

    plt.grid(color="gainsboro") # Сетка
    plt.legend(loc='upper right', fontsize=12) 
    plt.xlim([1000,6000])
    plt.ylim([0,4])
    plt.ylabel("t, с")
    plt.xlabel("N")
    plt.title("График зависимости t от N")
    fig = plt.gcf() # Взять текущую фигуру
    fig.set_size_inches(10, 10) # Задать размеры графика
    
    # Покажем окно с нарисованным графиком
    plt.show()
    fig.savefig("src/files/lab01_part02_manual.png")

