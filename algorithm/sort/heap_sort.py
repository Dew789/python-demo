
def heap_sort(t):
    length = len(t)
    min_root = length // 2 - 1
    for i in reversed(range(min_root)):
        _shift_down(t, i, length)
    for j in reversed(range(length)):
        t[j], t[0] = t[0], t[j]
        _shift_down(t, 0, j)


def _shift_down(t, root, end):
    child = 2 * root + 1
    while child < end:
        if child + 1 < end and t[child + 1] > t[child]:
            child += 1
        if t[child] < t[root]:
            break
        t[root], t[child] = t[child], t[root]
        root = child
        child = 2 * child + 1
