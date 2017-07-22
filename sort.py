from time import time
from random import randint


# Bubble Sort
def bubbleSort(t):
    check_length = len(t) - 1
    flag = 1
    while flag:
        flag = 0
        for i in range(check_length):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                check_length = i
                flag = 1

# Insertion Sort
def insertionSort(t):
    length = len(t)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if t[j] < t[j-1]:
                t[j], t[j-1] = t[j-1], t[j]
            else:
                break

# Shell Sort
def shellSort(t):
    length = len(t)
    gap = length
    while gap > 1:
        gap //= 2
        for i in range(gap, length):
            for j in range(i, 0, -gap):
                if t[j] < t[j-gap]:
                    t[j], t[j-gap] = t[j-gap], t[j]
                else:
                    break

# Selection Sort
def selectionSort(t):
    length = len(t)
    for i in range(length):
        min_pos = i
        for j in range(i+1, length):
            if t[j] < t[min_pos]:
                min_pos = j
        t[i], t[min_pos] = t[min_pos], t[i]

# Merge Sort
def mergeSort(t):
    length = len(t)
    if length == 1:
        return t
    mid = length // 2
    left = mergeSort(t[:mid])
    right = mergeSort(t[mid:])
    return merge(left, right)

def merge(left, right):
    length_left = len(left)
    lenght_right = len(right)
    i, j = 0, 0
    result = []
    while i < length_left and j < lenght_right:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < length_left:
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result

# Bucket Sort
def bucketSort():
    pass

# Quick Sort
def quickSort(t, front, rear):
    if front >= rear:
        return

    l, r = front, rear
    key = t[front]
    while r > l:
        while t[r] >= key and r > l:
            r -= 1
        t[l] = t[r]
        while t[l] < key and r > l:
            l += 1
        t[r] = t[l]
    t[r] = key
    quickSort(t, front, l-1)
    quickSort(t, r+1, rear)
    

# Heap Sort
def Heap_sort():
    pass

if __name__ == '__main__':
    a = [7, 8, 5, 1, 9, 2, 4, 6, 3, 10]
    #for i in range(10000):
    #    a.append(randint(1, 10000))
    print('Data ready')

    start = time()
    print(a)
    print(time()-start)
