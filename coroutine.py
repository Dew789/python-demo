def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


from time import sleep
import asyncio

@asyncio.coroutine
def hello():
    sleep(1)
    print("Hello world!")
    r = yield from asyncio.sleep(0.1)
    print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()