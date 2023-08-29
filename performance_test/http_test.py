import time
import requests
from concurrent.futures import ThreadPoolExecutor


def predict(url):
    while True:
        files = {'audioFile': open('D:/gyzn-data_f65e355f71c8_1_1_20230823_20230823152820791.pcm', 'rb')}
        payload = {'engineType': 'ae'}
        r = requests.post(url, files=files, data=payload)
        print(r.status_code)
        time.sleep(10)


def concurrent_http(url, count):
    pool = ThreadPoolExecutor(count)
    for i in range(1, count + 1):
        pool.submit(predict, url)

    while True:
        time.sleep(10)


if __name__ == "__main__":
    concurrent_http("http://10.40.152.198:8081/api/v1/predict", 100)
