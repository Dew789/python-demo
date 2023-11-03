from io import BytesIO

import requests

from scipy.io.wavfile import write
import numpy as np


def pcm_to_wav(pcm_data, bit_depth=32, sample_rate=48000, channel=1):
    wav_data = BytesIO()

    data_type = np.float32
    if bit_depth == 32:
        data_type = np.float32
    elif bit_depth == 16:
        data_type = np.int16

    array_a = np.frombuffer(pcm_data, dtype=data_type)

    write(wav_data, sample_rate, array_a)

    wav_data.seek(0)
    return wav_data


def get_audio_from_pcm(audio_url, bit_depth=32, sample_rate=48000, channel=1):
    r = requests.get(audio_url)

    return pcm_to_wav(r.content, bit_depth, sample_rate, channel)


def get_audio_from_wav(audio_url):
    r = requests.get(audio_url)

    return r.content
