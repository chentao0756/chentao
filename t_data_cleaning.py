import pandas as pd
import matplotlib.pyplot as plt

Real_estate_turnover = pd.read_csv("Real_estate_turnover.csv")
Real_estate_turnover.date = pd.to_datetime(Real_estate_turnover.date, format='%Y')
date = Real_estate_turnover.date
sale_volume = Real_estate_turnover.sale_volume
inventory = Real_estate_turnover.inventory

fig, ax = plt.subplots()
fig.set_size_inches([5,4])
ax.plot(date, sale_volume, marker = '*', color = 'b')
ax.plot(date, inventory, marker = 'o', linestyle = None, color = 'red')
ax.set_xlabel('Time')
ax.set_ylabel('sale_volume&inventory(hm²)')
ax.set_title('Real_estate_turnover')
plt.show()

