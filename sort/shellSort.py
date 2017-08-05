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
