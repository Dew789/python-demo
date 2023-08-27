
def merge_sort(t):
    length = len(t)
    if length == 1:
        return t
    mid = length // 2
    left = merge_sort(t[:mid])
    right = merge_sort(t[mid:])
    return merge(left, right)


def merge(left, right):
    l_length = len(left)
    r_length = len(right)
    i, j = 0, 0
    result = []
    while i < l_length and j < r_length:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < l_length:
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result
