def selectionSort(t):
    length = len(t)
    for i in range(length):
        min_pos = i
        for j in range(i+1, length):
            if t[j] < t[min_pos]:
                min_pos = j
        t[i], t[min_pos] = t[min_pos], t[i]
