
def insertion_sort(t):
    length = len(t)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if t[j] < t[j-1]:
                t[j], t[j-1] = t[j-1], t[j]
            else:
                break
