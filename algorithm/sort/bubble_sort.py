
def bubble_sort(t):
    check_length = len(t) - 1
    flag = 1
    while flag:
        flag = 0
        for i in range(check_length):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                check_length = i
                flag = 1


if __name__ == "__main__":
    data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(data)
    print(data)
