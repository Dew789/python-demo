import array
import numpy as np
import os
from math import log, exp
import librosa
import sys
import pandas as pd
from datetime import datetime
from pathlib import Path


# pcm_path = r'E:\新建文件夹\工业智能\风机叶片\株洲凤凰山\zhiting\783017485108322304_908352362954360832\1\202310\2023-10-18~00_05_59.pcm'#改
def readPCM(fileName):
    file = open(fileName, 'rb')
    pcm_data = array.array('h')
    size = int(os.path.getsize(fileName) / pcm_data.itemsize)
    pcm_data.fromfile(file, size)
    file.close()
    return np.array(pcm_data) / 32768


def read_condition(fileName):
    df = pd.read_excel(fileName)
    return df


def condition_decide(pcm_path, df: pd.DataFrame):
    d = pcm_path.split('\\')[-1].strip('.pcm')
    format_string = "%Y-%m-%d~%H_%M_%S"
    t = datetime.strptime(d, format_string)
    print(t)
    if df.loc[df[df.columns[0]] > t, '有功功率平均值(kW)'].values.shape[0] == 0:
        return True
    if df.loc[df[df.columns[0]] > t, '有功功率平均值(kW)'].values[0] < 5:
        return False
    else:
        return True


if __name__ == "__main__":
    # import pdb;pdb.set_trace()
    bladename = {'783017485108322304_908352362954360832': '201',
                 '783017485108322304_908348833191692288': '429',
                 '783017485108322304_904802439843547136': '318',
                 '783017485108322304_904797536656033792': '213',
                 '783017485108322304_908356093775185920': '201',
                 '783017485108322304_908355157690419200': '429',
                 '783017485108322304_908350761241937920': '318',
                 '783017485108322304_908353107569149952': '213',
                 '783017485108322304_908343821640140800': '201',
                 '783017485108322304_908351487309514752': '429',
                 '783017485108322304_908344985823741952': '318',
                 '783017485108322304_908354558009804800': '213',
                 '783017485108322304_908349838788659200': '201',
                 '783017485108322304_904783507422185472': '429',
                 '783017485108322304_908353879891511296': '318',
                 '783017485108322304_904800641124665344': '213',
                 }
    dict_blade = {'783017485108322304_908352362954360832': '201east',
                  '783017485108322304_908348833191692288': '429east',
                  '783017485108322304_904802439843547136': '318east',
                  '783017485108322304_904797536656033792': '213east',
                  '783017485108322304_908356093775185920': '201west',
                  '783017485108322304_908355157690419200': '429west',
                  '783017485108322304_908350761241937920': '318west',
                  '783017485108322304_908353107569149952': '213west',
                  '783017485108322304_908343821640140800': '201south',
                  '783017485108322304_908351487309514752': '429south',
                  '783017485108322304_908344985823741952': '318south',
                  '783017485108322304_908354558009804800': '213south',
                  '783017485108322304_908349838788659200': '201north',
                  '783017485108322304_904783507422185472': '429north',
                  '783017485108322304_908353879891511296': '318north',
                  '783017485108322304_904800641124665344': '213north',
                  }

    pcm_path = sys.argv[1]
    data = readPCM(pcm_path)
    rms = librosa.feature.rms(y=data)
    fenbei = 20 * log(rms.sum() / rms.shape[1], 10)
    if fenbei > -66:
        print('status: working!')
        # print(f"copy {os.path.join(Path(pcm_path))} {local_path}")
    else:
        print('status: stop!')

    # filepath = sys.argv[1]
    # fileout = f'{sys.argv[1]}_step2.bat'
    # # local_path = '213_east'

    # with open(filepath,'r') as f, open(fileout,'w') as fo:
    #     for line in f.readlines():
    #         pcm_path = line.strip()
    #         if not pcm_path.endswith('pcm'):
    #             continue
    #         local_path = dict_blade[Path(pcm_path).parts[-4]]
    #         local_path = os.path.join('20231101_1115',local_path,Path(pcm_path).parts[-2])
    #         if not os.path.exists(local_path):
    #             os.makedirs(local_path)
    #         data = readPCM(pcm_path)
    #         rms = librosa.feature.rms(y=data)
    #         # sum_ = 0
    #         # for k in range(len(data)):
    #         # 	sum_+= abs(data[k])
    #         # sum_ = sum_/len(data)
    #         # print(len(data),max(data),min(data),sum(data>=0),len(data),data.shape)

    #         # fenbei = 20*log(max(data)/65535,10)
    #         # fenbei = 20*log(sum_,10)
    #         fenbei = 20*log(rms.sum()/rms.shape[1],10)
    #         # import pdb;pdb.set_trace()

    #         if fenbei > -66 :
    #             # print('fenbei = ',fenbei)
    #             print(f"copy {os.path.join(Path(pcm_path))} {local_path}")
    #             fo.write(f"copy {os.path.join(Path(pcm_path))} {local_path}")
    #             fo.write('\n')
    #         else:
    #             pass
