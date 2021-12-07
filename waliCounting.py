import pandas as pd
import os
c = ['年紀一','年紀二','相對瓦力','wa值','絕對瓦力']
try:
    y11 = int(input('輸入年紀一起始值'))
    y12 = int(input('輸入年紀一結束值'))
    y21 = int(input('輸入年紀二起始值'))
    y22 = int(input('輸入年紀二結束值'))
except ValueError:
    print('請輸入整數')
    os.system('pause')
    exit()
s = []
for loop1 in range(y11,y12):
    for loop2 in range (y21,y22):
        Rwali = loop2 - loop1
        if loop2 > loop1:
            Cwali = abs(Rwali) / loop1
        else:
            Cwali = abs(Rwali) / loop2
        Awali = Rwali * Cwali
        s.append([loop1,loop2,Rwali,Cwali,Awali])
df = pd.DataFrame(s,columns=c)
print(df)
i = input('是否列印y/n：')
if i == 'y':
    df.to_csv('.\瓦力計算.csv',encoding='utf_8_sig', index = False)
    print('檔案存為 瓦力計算.csv')
os.system('pause')