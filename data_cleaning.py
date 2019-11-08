import pandas as pd
import matplotlib.pyplot as plt

housingprice = pd.read_csv("HousingPriceZH.csv", encoding="GB2312")

for i in range(len(housingprice.date)):
    housingprice.date[i] = housingprice.date[i].replace("年", "-").replace("月", "")
    print(housingprice.head())
housingprice.date = pd.to_datetime(housingprice.date)

plt.plot(housingprice.date, housingprice.avg_price)
plt.xlabel("Time")
plt.ylabel("avg_price(CNY/m²)")
plt.show()



