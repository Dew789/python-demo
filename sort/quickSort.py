from random import randint

def quick_sort(t, font, rear):
    if font >= rear:
        return
    pivot = t[font]
    index = font;
    for i in range(font, rear+1):
        # have to skip pivot, we need it here
        if i == font:
            index += 1
        if t[i] < pivot:
            temp = t[index]
            t[index] = t[i]
            t[i] = temp
            index += 1
    # the index is always the bigger number than pivot
    # but we have to swap the small one
    if index > font:
        index -= 1
    temp = t[index]
    t[font] = temp
    t[index] = pivot
    quick_sort(t, font, index)
    quick_sort(t, index+1, rear)


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
    for i in range(1000):
        t.append(i)
    from time import time
    start = time()
    randomized_quick_sort(t, 0, 999)
    print(time() - start)
    start = time()
    quick_sort(t, 0, 999)
    print(time()-start)
