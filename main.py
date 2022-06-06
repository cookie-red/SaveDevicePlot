# 執行環境Pytion V3.8
import pandas as pd
import matplotlib.pyplot as plt
import glob,os

# print(glob.glob(os.path.join("Folder_1", "*.txt")))

for i in glob.glob(os.path.join("0605","*.csv")): # ("資料夾名稱","所選檔案格式")
    # 字串分割
    str = i.split('.csv')
    # 讀取資料夾內的CSV
    df = pd.read_csv(i)
    index = df.index
    accx = []
    accy = []
    accz = []
    Gv = []
    pitch = []
    state = []

    for i in df['ACC_X']:
        i = round(i *512 ,2)
        accx.append(i)
    df['accX'] = accx
    accX = df['accX']

    for i in df['ACC_Y']:
        i = round(i * 512,2)
        accy.append(i)
    df['accY'] = accy
    accY = df['accY']

    for i in df['ACC_Z']:
        i = round(i * 512,2)
        accz.append(i)
    df['accZ'] = accz
    accZ = df['accZ']

    for i in df['G_Value']:
        i = round(i *512 ,2)
        Gv.append(i)
    df['gvalue'] = Gv
    Gvalue = df['gvalue']

    for i in df['Pitch']:
        i = round(i *10 ,2)
        pitch.append(i)
    df['pitch'] = pitch
    Pitch = df['pitch']

    for i in df['state']:
        i = round(i *100 ,2)
        state.append(i)
    df['state'] = state
    state = df['state']

    fig = plt.figure()
    plt.plot(index,accX,color='b', label = 'ACC_X')
    plt.plot(index,accY,color='darkorange', label = 'ACC_Y')
    plt.plot(index,accZ,color='y', label = 'ACC_Z')
    plt.plot(index,Gvalue,color='g', label = 'G_value')
    plt.plot(index,Pitch,color='slategray', label = 'Pitch')
    plt.plot(index,state,color='r', label = 'state')
    plt.axhline(y=600, color='m', linestyle='--', label = 'Stand_threshold')
    plt.axhline(y=450, color='dodgerblue', linestyle='--', label = 'Sit_threshold')
    plt.axhline(y=280, color='chocolate', linestyle='--', label = 'all_down_threshold')
    plt.xlabel("Time(ms)")
    y_major_locator = plt.MultipleLocator(200)
    ay = plt.gca()
    ay.yaxis.set_major_locator(y_major_locator)
    plt.legend()
    plt.title(str[0])
    plt.grid()
    # 設定圖表為16:9的尺寸
    fig.set_figheight(9)
    fig.set_figwidth(16)
    plt.savefig(str[0]+".png", dpi = 120, bbox_inches='tight') # 調整另存圖檔的比例
    plt.show()