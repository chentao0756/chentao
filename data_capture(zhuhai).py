import csv
import urllib.request
import re

url_list = ["https://www.anjuke.com/fangjia/zh201{}/".format(i) for i in range (1,10)]

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}

f = open("HousingPriceZH.csv", "w", newline='')
writer = csv.writer(f)
writer.writerow(("date", "avg_price"))

for url in url_list:
    HTMLtxt = urllib.request.urlopen(url).read().decode('utf-8').strip()
    data = re.findall(r'<li.*?<a.*?class="nostyle">.*?<b>(.*?)房价</b>.*?<span>(.*?)元/㎡</span>.*?<em>.*?</em>.*?</a>.*?</li>', HTMLtxt, re.S)
    for a in data:
        date = a[0]
        price = a[1]
        writer.writerow((date, price))

f.close()
