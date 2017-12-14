from random import randint

def quick_sort(t, front, rear):
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
    quick_sort(t, front, l-1)
    quick_sort(t, r+1, rear)

def randomized_quick_sort(t, front, rear):
    """ 
        if imput array is sorted, 
        common quick sort will be O(n^2).
        randomized the povit would make complexity to O(nlogn).
    """
    if front >= rear:
        return
    rand_index = randint(front, rear)
    povit = t[rand_index]
    i = front
    for index in range(front, rear+1):
        # Don't swap povit
        if i == rand_index:
            i += 1
        if t[index] < povit:
            temp = t[i]
            t[i] = t[index]
            t[index] = temp
            i += 1
    # Based on i to swap povit
    if i > rand_index:
        i -= 1
    temp = t[i]
    t[i] = povit
    t[rand_index] = temp
    randomized_quick_sort(t, front, i)
    randomized_quick_sort(t, i+1, rear)
    

if __name__ == '__main__':
    t = []
    for i in range(10000000):
        t.append(i)
    from time import time
    start = time()
    randomized_quick_sort(t, 0, 99)
    print(time() - start)
    start = time()
    quick_sort(t, 0, 99)
    print(time()-start)
