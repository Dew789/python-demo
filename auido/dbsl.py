import numpy as np
import scipy.io.wavfile as wav
from math import isinf


def get_a_weight(freq):
    """
    参考文档：
     https://blog.csdn.net/qq_30432883/article/details/105460241
     https://www.ntiaudio.cn/%E5%AE%A2%E6%88%B7%E6%94%AF%E6%8C%81/%E6%8B%93%E5%B1%95/%E5%A3%B0%E5%8E%8B%E7%BA%A7%E6%B5%8B%E9%87%8F%E4%B8%AD%E7%9A%84%E9%A2%91%E7%8E%87%E8%AE%A1%E6%9D%83/
    """
    a_weight = {
        (0, 8): -77.8,
        (8, 16): -56.7,
        (16, 32): -39.4,
        (32, 63): -26.2,
        (63, 125): -16.1,
        (125, 250): -8.6,
        (250, 500): -3.2,
        (500, 1000): 0,
        (1000, 2000): 1.2,
        (2000, 4000): 1,
        (4000, 8000): -1.1,
        (8000, 16000): -6.6
    }
    for (start, end), db in a_weight.items():
        if start < freq <= end:
            return db
    return -10


def a_weight_filter(file_path, new_file_path):
    rate, data = wav.read(file_path)
    fft_data = np.fft.fft(data)
    a_weight_fft_data = []
    for i in range(0, len(fft_data)):
        a_weight_fft_data.append(fft_data[i] + get_a_weight(i))

    ifft_data = np.fft.ifft(a_weight_fft_data).astype(np.int16)
    wav.write(new_file_path, rate, ifft_data)


def cal_db(file_path):
    with open(file_path, "rb") as f:
        dBSPL = []
        audio_data = np.fromfile(f, dtype=np.int16)[0: 1 * 48000]

        for data in audio_data:
            result = (10 * np.log10(np.square(10 / 6.59 * 2 / 0.04 * data)) + 94)
            if not isinf(result):
                dBSPL.append(result)
            # 每0.1s进行一次数据计算
            if len(dBSPL) == 4800:
                print(np.mean(dBSPL))
                dBSPL = []


def pcm2wav(pcm_path, out_path, channel, sample_rate):
    with open(pcm_path, 'rb') as pcm_file:
        pcm_data = pcm_file.read()
        pcm_file.close()
    with wave.open(out_path, 'wb') as wav_file:
        wav_file.setparams((channel, 16 // 8, sample_rate, 0, 'NONE', 'NONE'))
        wav_file.writeframes(pcm_data)
        wav_file.close()
