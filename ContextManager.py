from contextlib import contextmanager, closing
from time import time, sleep
import requests


# With 
class Timer(object):

    def __init__(self, verbose=False, ignoreException=False):
        self.verbose = verbose
        self.ignoreException = ignoreException

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.end = time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if self.verbose:
            print("elapsed time: %f ms" % self.msecs)
    
        return self.ignoreException

def exception_test():
    try:        
        with Timer(True, False):
            raise Exception("Ex4Test")
    except Exception, e:
        print "Exception (%s) was caught" %e
    else:
        print "No Exception happened"

# contextmanager
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# closing
with closing(requests.get('https://www.python.org')) as page:
    for line in page:
        print(line)

if __name__ == '__main__':
    with create_query("ff") as e:
        e.query()
