import array
import numpy as np
import os
from math import log, exp
import librosa
import sys


def readPCM(fileName):
    file = open(fileName, 'rb')
    pcm_data = array.array('h')
    size = int(os.path.getsize(fileName) / pcm_data.itemsize)
    pcm_data.fromfile(file, size)
    file.close()
    return np.array(pcm_data) / 32768


if __name__ == "__main__":
    pcm_path = sys.argv[1]
    data = readPCM(pcm_path)
    rms = librosa.feature.rms(y=data)
    fenbei = 20 * log(rms.sum() / rms.shape[1], 10)
    if fenbei > -39:
        print('status: working!')
    else:
        print('status: stop!')
