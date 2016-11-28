import requests
import json
from multiprocessing import Pool
import os, time, random

url = 'http://www.example.com'
user = 'example_user'
pwd = 'example_pass'

headers = {"Accept":"application/json"}

def recive(addr):
    response = requests.get(url, auth=(user, pwd), headers=headers)

    with open(r'C:\Users\user\Desktop\%s.json'%addr, 'w') as e:
        recive = json.dumps(response.json(), indent=2)
        e.write(recive)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(100):
        p.apply_async(recive, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')