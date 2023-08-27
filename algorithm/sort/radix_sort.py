import math


def radix_sort_lsd(t):
    K = math.ceil(math.log(max(t), 10))
    bucket = [[] for i in range(10)]

    for i in range(1, K+1):
        for val in t:
            bucket[val % (10**i) // (10**(i-1))].append(val)
        del t[:]
        for each in bucket:
            t.extend(each)
        bucket = [[] for i in range(10)]


def radix_sort_msd(t):
    K = math.ceil(math.log(max(t), 10))
    return sort(t, K)


def sort(t, K):
    result = []
    if K == 0:
        return t
    bucket = [[] for i in range(10)]
    for val in t:
        bucket[val % (10**K) // (10**(K-1))].append(val)
    K -= 1
    for sub_bucket in bucket:
        outcome = sort(sub_bucket, K)
        if outcome:
            result.extend(outcome)
    return result
