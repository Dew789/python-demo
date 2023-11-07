from scipy.signal import butter, filtfilt, hilbert, argrelmax, argrelmin,find_peaks
import numpy as np
import matplotlib.pyplot as plt
import array
import os


def find_diuzhen(file_name):
    x = readPCM(file_name)
    b, a = butter(8, [1000 / (48000 / 2), 20000 / (48000 / 2)], 'bandpass')
    x = filtfilt(b, a, x)

    x = np.diff(x, n=2)
    if (x > 0.00075).sum() > 10:
        return file_name + "," + "loss: %s" % (x > 0.00075).sum()
    else:
        return file_name + "," + "no loss"


def readPCM(file_name):
    file = open(file_name, 'rb')
    pcm_data = array.array('h')
    size = int(os.path.getsize(file_name) / pcm_data.itemsize)
    pcm_data.fromfile(file, size)
    file.close()
    return np.array(pcm_data) / 32768

# import pdb;pdb.set_trace()
# x = readPCM(r'C:\Users\leiwang32\Desktop\2023-10-18~19_04_12.pcm')
# x = readPCM(r'C:\Users\leiwang32\Desktop\2023-10-18~00_00_59.pcm')
# x = readPCM(r'C:\Users\leiwang32\Desktop\2023-10-19~12_30_15.pcm')
# x = readPCM(r'C:\Users\leiwang32\Desktop\2023-10-18~15_30_57 (2).pcm')
# b, a = butter(8, [1000 / (48000 / 2),20000 / (48000 / 2)], 'bandpass')
# b, a = butter(8, 2000 / (sr / 2), 'highpass')
# x = filtfilt(b, a, x) #signal为要过滤的信号

# x1 = np.roll(x,-1)
# std_all = np.std(x)
# print(f'std: {std_all}')
##二阶差分
# x = np.diff(x, n=2)
# if (x>0.00075).sum()  > 10:
#     print(f'丢帧:{(x>0.00075).sum()}')
# std_all = np.std(x)
# print(f'std: {std_all}')
# x = (x-np.min(x))/(np.max(x)-np.min(x))  # 最值归一化
# x = (x-np.mean(x))/(np.max(x)-np.min(x))  # 最值归一化
# x = (x-np.mean(x))/(np.std(x))  # 最值归一化

# t = np.arange(len(x))
# std_all = np.std(x)
# print(f'std: {std_all}')
# thresh_top = np.median(x) + 1 * np.std(x)
##分位数
# thresh_top = np.percentile(x,(25)) 
# thresh_bottom = np.percentile(x,(75))
# q1 = np.percentile(x,(25)) 
# q2 = np.percentile(x,(50)) 
# q3 = np.percentile(x,(75)) 
# up_xu = q3+1.5*(q3-q1)
# down_xu = q1-1.5*(q3-q1)
# num_e = (x>up_xu).sum()+(x<down_xu).sum()
# print(num_e)
###
# thresh_top = 0.95
# thresh_bottom = 0.95
# (you may want to use std calculated on 10-90 percentile data, without outliers)

# Find indices of peaks
# peak_idx, _ = find_peaks(x, prominence=0.5)
# peak_idx, _ = find_peaks(x, wlen=3.1,prominence=0.3)

# # Find indices of valleys (from inverting the signal)
# valley_idx, _ = find_peaks(-x, wlen=3.1, prominence=0.3)
# print(f'peaks:{len(peak_idx)+len(valley_idx)}')
# # Plot signal
# # plt.figure(1)
# # plt.boxplot(x)
# # plt.show()
# plt.figure(2)
# plt.plot(t, x   , color='b', label='data')
# plt.scatter(t, x, s=10,c='b',label='value')

# # Plot threshold
# # plt.plot([min(t), max(t)], [thresh_top, thresh_top],   '--',  color='r', label='peaks-threshold')
# # plt.plot([min(t), max(t)], [thresh_bottom, thresh_bottom], '--',  color='g', label='valleys-threshold')

# # Plot peaks (red) and valleys (blue)
# plt.plot(t[peak_idx], x[peak_idx],     "x", color='r', label='peaks')
# plt.plot(t[valley_idx], x[valley_idx], "x", color='g', label='valleys')

# plt.xticks(rotation=45)
# plt.ylabel('value')
# plt.xlabel('timestamp')
# plt.title(f'data over time for username=target')
# plt.legend( loc='upper left')
# plt.gcf().autofmt_xdate()

# plt.show()


if __name__ == "__main__":
    with open(r"D:\株洲4g-429.csv", "w") as e:
        for root, dirs, files in os.walk(r"D:\audio"):
            for file in files:
                result = find_diuzhen(os.path.join(root, file))
                e.write(result)
                e.write("\n")