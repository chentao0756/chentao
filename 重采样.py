import pandas as pd
import matplotlib.pyplot as plt

housingprice = pd.read_csv("HousingPriceZH.csv", encoding="GB2312")

for i in range(len(housingprice.date)):
    housingprice.date[i] = housingprice.date[i].replace("年", "-").replace("月", "")

housingprice.date = pd.to_datetime(housingprice.date)
housingprice = housingprice.set_index(housingprice["date"])
hp = housingprice.resample('A').mean()

Real_estate_turnover = pd.read_csv("Real_estate_turnover.csv")
Real_estate_turnover.date = pd.to_datetime(Real_estate_turnover.date, format='%Y')


date = Real_estate_turnover.date
sale_volume = Real_estate_turnover.sale_volume
inventory = Real_estate_turnover.inventory

fig, ax = plt.subplots(2,1,sharex=True)
ax[1].plot(date, sale_volume, marker = '*', color = 'b')
ax[1].plot(date, inventory, marker = '*', linestyle = None, color = 'red')
ax[0].plot(hp, marker = '*', color = 'c')

plt.show()

