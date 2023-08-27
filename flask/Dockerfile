FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/

COPY app ./app
COPY run.py boot.sh ./
RUN chmod 755 boot.sh

CMD [ "bash", "boot.sh" ]
