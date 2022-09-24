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
