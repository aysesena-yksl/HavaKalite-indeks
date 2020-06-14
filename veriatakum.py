from google.colab import drive
drive.mount("/content/drive")

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sea
data = pd.read_excel("/content/drive/My Drive/YMGK/denemeatakum.xlsx")
data['PM10'] = data['PM10'].astype('float')
data['SO2'] = data['SO2'].astype('float')
data['NO2'] = data['NO2'].astype('float')
data['O3'] = data['O3'].astype('float')
data['katıatık'] = data['katıatık'].astype('float')



print(data.mean())

data = data.fillna(data.mean())


plt.figure(figsize=(12,6))
plt.plot(data.Tarih,data.atıkkatı)
plt.show()


plt.figure(figsize=(24,12))
plt.subplot(2,2,1)
plt.plot(data.Tarih,data.PM10,color="red")
plt.plot(data.Tarih,data.SO2,color="blue")
plt.plot(data.Tarih,data.NO2,color="black")
plt.plot(data.Tarih,data.O3,color="orange")
plt.plot(data.Tarih,data.katıatık,color="yellow")

plt.xlabel("Tarih")
plt.ylabel("PM10-SO2-NO2-O3 Miktarı")
plt.title("Zamana Göre PM10(Red)-SO2(Blue)-CO(Black)-NO2(Orange) değişimi")

plt.subplot(2,2,2)
plt.plot(data.Tarih,data.SO2,color="blue")
plt.xlabel("Tarih")
plt.ylabel("KATI YOĞUNLUĞU")
plt.title("Zamana Göre Atık değişimi")

plt.show()



sea.scatterplot(x ="NO2",y="PM10", data=data)
plt.show()
sea.scatterplot(x ="PM10",y="atıkkatı", data=data)
plt.show()
