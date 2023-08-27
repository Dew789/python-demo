import requests
import json
from process import Pool, Process, Queue
import os, time, random

url = 'http://www.example.com'
user = 'example_user'
pwd = 'example_pass'

headers = {"Accept":"application/json"}


def receive(addr):
    response = requests.get(url, auth=(user, pwd), headers=headers)

    with open(r'C:\Users\user\Desktop\%s.json'%addr, 'w') as e:
        data = json.dumps(response.json(), indent=2)
        e.write(data)


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['1', '2', '3']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(100):
        p.apply_async(receive, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.terminate()