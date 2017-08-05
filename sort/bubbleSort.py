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
