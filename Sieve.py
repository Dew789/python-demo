def _int_iter(m):
    n = 1
    for i in range(2, m):
        yield i

def _not_divisiable(n):
    return lambda x: x % n > 0

def sieve(m):
    it = _int_iter(m)
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n), it)
