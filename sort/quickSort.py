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
