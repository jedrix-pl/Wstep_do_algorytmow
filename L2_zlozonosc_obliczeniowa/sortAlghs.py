import random
import time
from matplotlib import pyplot as plt


def bubbleSort1(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


def bubbleSort2(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True

    return arr


def bubbleSort3(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        curr_element = arr[i]
        j = i - 1
        while j >= 0 and curr_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr_element

    return arr


def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def avg(list):
    return sum(list) / len(list)


def runTime(arrLenght, specs=False):
    arr = [random.randint(0, 100) for g in range(arrLenght)]


    bubble_times = []
    insertion_times = []
    selection_times = []

    for z in range(10):
        start_time = time.time()
        bubbleSort1(arr)
        bubble_times.append((time.time() - start_time))

        start_time = time.time()
        insertionSort(arr)
        insertion_times.append(time.time() - start_time)

        start_time = time.time()
        selectionSort(arr)
        selection_times.append((time.time() - start_time))

    if specs:
        print(f"""
            ({len(arr)} elements)
        
        Bubble sort average time: {format(avg(bubble_times), '.7f')}s
        Bubble sort max time: {format(max(bubble_times), '.7f')}s
        
        Insertion sort average time: {format(avg(insertion_times), '.7f')}s
        Insertion sort max time: {format(max(insertion_times), '.7f')}s
        
        Selection sort average time: {format(avg(selection_times), '.7f')}s
        Selection sort max time: {format(max(selection_times), '.7f')}s""")

    bubble = [format(avg(bubble_times), '.7f'), format(max(bubble_times), '.7f')]
    insertion = [format(avg(insertion_times), '.7f'), format(max(insertion_times), '.7f')]
    selection = [format(avg(selection_times), '.7f'), format(max(selection_times), '.7f')]

    return bubble, insertion, selection



if __name__ == "__main__":
    n = [10, 20, 50, 100, 200, 500, 1000]

    bubble_avg = []
    bubble_max = []

    insertion_avg = []
    insertion_max = []

    selection_avg = []
    selection_max = []

    for c in range(len(n)):
        curr_run = runTime(n[c], specs=True)

        bubble_avg.append(curr_run[0][0])
        bubble_max.append(curr_run[0][1])

        insertion_avg.append(curr_run[1][0])
        insertion_max.append(curr_run[1][1])

        selection_avg.append(curr_run[2][0])
        selection_max.append(curr_run[2][1])


    plt.figure(figsize=(12, 8))
    plt.subplot(321)
    plt.bar(n, bubble_avg, width=6.0)
    plt.xlabel('Number of elements')
    plt.ylabel('Time[s]')
    plt.title('Bubble sort AVG')
    plt.subplot(322)
    plt.bar(n, bubble_max, width=6.0)
    plt.xlabel('Number of elements')
    plt.ylabel('Time[s]')
    plt.title('Bubble sort MAX')
    plt.subplot(323)
    plt.bar(n, insertion_avg, width=6.0)
    plt.xlabel('Number of elements')
    plt.ylabel('Time[s]')
    plt.title('Insertion sort AVG')
    plt.subplot(324)
    plt.bar(n, insertion_max, width=6.0)
    plt.xlabel('Number of elements')
    plt.ylabel('Time[s]')
    plt.title('Insertion sort MAX')
    plt.subplot(325)
    plt.bar(n, selection_avg, width=6.0)
    plt.xlabel('Number of elements')
    plt.ylabel('Time[s]')
    plt.title('Selection sort AVG')
    plt.subplot(326)
    plt.bar(n, selection_max, width=6.0)
    plt.xlabel('Number of elements')
    plt.ylabel('Time[s]')
    plt.title('Selection sort MAX')
    plt.show()


    arr = [random.randint(0, 100) for g in range(1500)]

    time_zero = time.time()
    bubbleSort1(arr)
    time_end1 = time.time() - time_zero

    time_zero = time.time()
    bubbleSort2(arr)
    time_end2 = time.time() - time_zero

    time_zero = time.time()
    bubbleSort3(arr)
    time_end3 = time.time() - time_zero

    print(f"""
 - Bubble sorting algorithms time comparison -

bubbleSort1: {format(time_end1, '.7f')}s
bubbleSort2: {format(time_end2, '.7f')}s
bubbleSort3: {format(time_end3, '.7f')}s""")