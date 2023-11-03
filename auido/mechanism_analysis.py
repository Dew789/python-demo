import math

import numpy as np
from scipy.io import wavfile

np.set_printoptions(suppress=True)


# TODO 没有做边界检查
# 粗暴的去噪算法， TODO 这个地方有待商榷
# 倍频和倍频计算范围算作有效声音，如果倍频为50，倍频计算范围10，
# 非倍频范围内均视为噪声，比如45-55HZ, 95-105HZ ... 之外的声音
FREQ_MULTIPLIER = 50
FREQ_MULTIPLIER_RANGE = 10


class Analysis:

    normalize_value = 48000

    def __init__(self, audio_path):
        # 返回FFT后的每个频率对应的幅值
        # 频率精度为1Hz, 频率范围为0 ~ 采样率/2
        self.spectrum = self.get_spectrum(audio_path)
        # 计算频率上限
        self.high = 2000 if len(self.spectrum) > 2000 else len(self.spectrum)

    @staticmethod
    def get_index(start, end, step, scope):
        index = []
        for i in range(start, end, step):
            for j in range(i - scope // 2, i + scope // 2 + 1):
                index.append(j)

        return index

    @classmethod
    def get_spectrum(cls, audio):
        """
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
        https://www.zhihu.com/question/20977844/answer/651196756
        https://blog.csdn.net/xufive/article/details/105321849
        FFT和RFFT的区别: https://numpy.org/doc/1.22/reference/generated/numpy.fft.rfft.html
        FFT size : https://www.zhihu.com/question/276261013
        每个值代表0-24000Hz的幅值大小

        优化项目：
            1. 加窗
            2. 移帧
        """
        # 获取原始音频数据
        rate, data = wavfile.read(audio)
        num = data.shape[0] // rate
        print("原始音频采样率 %d, 通道数 %d, 音频时长(精确到秒) %d" % (rate, len(data.shape), num))

        data1 = data[0:num * rate].reshape(num, rate)

        xfp = 0
        for i in range(num):
            xf = np.fft.rfft(data1[i, :]) / cls.normalize_value  # 归一化处理数据值
            if i == 0:
                xfp = np.abs(xf)
            else:
                xfp += np.abs(xf)

        xfp = xfp / num
        return xfp

    @classmethod
    def compare(cls, audio_path1, audio_path2):
        x1 = cls.get_spectrum(audio_path1)
        x2 = cls.get_spectrum(audio_path2)

        start = 0
        end = len(x1) // 50

        dividend = 0
        divisor = 0
        for i in range(start, end):
            dividend += (x1[i * 50] - x2[i * 50]) ** 2
            divisor += x1[i * 50]

        comparison = math.sqrt(dividend) / divisor

        return round(comparison, 4)

    def basic_frequency(self):
        """
        主频
        :return:
        """

        return np.argmax(self.spectrum)

    def fundamental_frequency_rate(self):
        """
        基频比重
        """
        low = 50

        fund_req = self.spectrum[100]
        index = self.get_index(low, self.high + 1, FREQ_MULTIPLIER, FREQ_MULTIPLIER_RANGE)
        sum_f = sum(self.spectrum[index])

        return round(fund_req / sum_f, 4)

    def fifty_multiplier_rate(self):
        """
        50Hz 奇偶次倍频比
        """

        odd_index = np.arange(50, self.high - 50 + 1, 100)
        even_index = np.arange(100, self.high + 1, 100)
        sum_odd = sum(self.spectrum[odd_index])
        sum_even = sum(self.spectrum[even_index])

        return round(sum_odd / sum_even, 4)

    def vibrational_entropy(self):
        """
        振动熵
        """

        lf_total = sum(i ** 2 for i in self.spectrum[np.arange(100, self.high + 1, 100)])

        result = 0
        for i in self.get_index(100, self.high + 1, FREQ_MULTIPLIER, FREQ_MULTIPLIER_RANGE):
            lf = self.spectrum[i] ** 2 / lf_total
            if lf == 0:
                continue
            result += lf * np.log2(lf)

        return round(np.abs(result), 4)

    def high_low_rate(self):
        """
        高低频比
        :return:
        """
        high_low_threshold = 700
        low = 50

        low_index = self.get_index(low, high_low_threshold, FREQ_MULTIPLIER, FREQ_MULTIPLIER_RANGE)
        high_index = self.get_index(high_low_threshold, self.high + 1, FREQ_MULTIPLIER, FREQ_MULTIPLIER_RANGE)

        return round(sum(self.spectrum[high_index]) / sum(self.spectrum[low_index]), 4)


if __name__ == "__main__":
    analysis = Analysis()
    # result = analysis.compare(
    #     r"C:\Users\hangzhang2\Desktop\项目\音频分析\audio\s1.wav",
    #     r"C:\Users\hangzhang2\Desktop\项目\音频分析\audio\s2.wav")

    result = analysis.compare(
        r"D:\声音成分变化量检测\13-11.44\benchmark.wav",
        r"D:\声音成分变化量检测\13-11.44\compare.wav")
    print(result)
