import csv
import urllib.request
import re


url_list_R = []
with open("url.txt", "r") as a:
    for line in a:
        url_list_R.append(list(line.strip('\n').split(',')))

# headers = {
#      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}

b = open("Real_estate_turnover.csv", "w", newline='')
writer = csv.writer(b)
writer.writerow(("date", "sale_volume", "inventory"))

for url in url_list_R:
    print(url)
    html_txt = urllib.request.urlopen(url).read().decode('utf-8').strip()
    data = re.findall(r'<div>.*?商品房销售面积(.*?)万平方米.*?商品房待售面积(.*?)万平方米', html_txt, re.S)
    for c in data:
        sale_volume = c[0]
        inventory = c[1]
        writer.writerow((sale_volume, inventory))

b.close()
