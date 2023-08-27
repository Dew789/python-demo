import string


def process_file(file_addr):
    hist = dict()
    fp = open(file_addr)

    for line in fp:
        process_line(line, hist)

    return hist


def process_line(line, hist):
    line = line.replace('-', '')

    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1


def total_words(hist):
    return sum(hist.values())


def differner_words(hist):
    return len(hist)


def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t


def subtract_1(d1, d2):
    """
    Returns a dictionary of all keys appear d1 but not d2

    d1, d2: dictionaries
    """
    return set(d1) - set(d2) 


def subtract_2(d1, d2):
    """
    Returns a dictionary of all keys appear d1 but not d2

    d1, d2: dictionaries
    """
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


if __name__ == '__main__':
    hist = process_file(r'emma.txt')