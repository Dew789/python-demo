def make_heap(t):
    length = len(t)
    minest_root = length // 2 - 1
    for i in range(minest_root, -1 ,-1):
        _sift_up(t, i, length)

def _sift_up(t, root, end):
    child = 2 * root + 1
    temp = t[root]
    while child < end:
        if child + 1 < end and t[child + 1] < child:
            child += 1
        if t[child] > t[root]:
            break
        t[root] = t[child]
        root = child
        child = 2 * child + 1
    t[root] = temp
