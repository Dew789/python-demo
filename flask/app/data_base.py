#!/usr/bin/env python3
# encoding: utf-8
"""
Refrence:
    1. https://docs.python.org/3.7/library/io.html
There's more thing we should notice in a real data-base:
    1.write partial document
    2.concurrent document modify
"""
import json
import os
import uuid


class DataBase(object):

    def __init__(self, data_dir="./data"):
        self.data_file = os.path.join(data_dir, "t.d")
        self.index_file = os.path.join(data_dir, "t.i")
        self.index = {}
        self.clear()
        if os.path.exists(self.index_file):
            with open(self.index_file, "r") as e:
                self.index = json.loads(e.read())

    def clear(self):
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        if os.path.exists(self.index_file):
            os.remove(self.index_file)

    def set(self, key, value):
        with open(self.data_file, "a") as e:
            pos = e.tell()
            size = e.write(str(key) + "," + str(value) + "\n")
            self.index[key] = (pos, size)
        with open(self.index_file, "w") as e:
            e.write(json.dumps(self.index))

    def get(self, key):
        item = ""
        key_str = str(key)
        pos, offset = self.index.get(key, (None, None))
        with open(self.data_file, "r") as e:
            if pos is not None and offset is not None:
                e.seek(pos)
                item = e.read(offset)

            # for line in e.readlines():
            #     if line.startswith(key):
            #         item = line

        return item[len(str(key_str)) + 1: -1] if item else None


if __name__ == "__main__":
    db = DataBase()
    for i in range(1, 1000):
        db.set(i, uuid.uuid4())

    assert(db.get(1) == "Beijing")
    assert(db.get(2) == "Tianjin")
    assert(db.get(3) == "Hubei")

    print(db.get(4))