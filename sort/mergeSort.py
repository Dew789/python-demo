def mergeSort(t):
    length = len(t)
    if length == 1:
        return t
    mid = length // 2
    left = mergeSort(t[:mid])
    right = mergeSort(t[mid:])
    return merge(left, right)

def merge(left, right):
    length_left = len(left)
    lenght_right = len(right)
    i, j = 0, 0
    result = []
    while i < length_left and j < lenght_right:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < length_left:
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result
