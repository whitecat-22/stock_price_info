from bs4 import BeautifulSoup
import requests
import csv

# Yahoo!finance から銘柄コードを配列に

# ストップ高 最大50銘柄
# url = "https://info.finance.yahoo.co.jp/ranking/?kd=27&mk=1&tm=d&vl=a"

# ストップ安 最大50銘柄
# url = "https://info.finance.yahoo.co.jp/ranking/?kd=28&mk=1&tm=d&vl=a"

# 値上がり率 1-50位
url = "https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=1&tm=d&vl=a"

# 値下がり率 1-50位
# url = "https://info.finance.yahoo.co.jp/ranking/?kd=2&mk=1&tm=d&vl=a"

# 出来高 1-50位
# url = "https://info.finance.yahoo.co.jp/ranking/?kd=3&mk=1&tm=d&vl=a"

l = list()
t = list()
num = 1
while num <= 51:
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

# ストップ高 最大50銘柄
#    codes = soup.select("#contents-body-bottom > div.rankdata > div.rankingTableWrapper > table > tbody > tr:nth-child(" + str(num) + ") > td:nth-child(1) > a")

# ストップ安 最大50銘柄
#    codes = soup.select("#contents-body-bottom > div.rankdata > div.rankingTableWrapper > table > tbody > tr:nth-child(" + str(num) + ") > td:nth-child(1) > a")

# 値上がり率 1-50位
    codes = soup.select("#contents-body-bottom > div.rankdata > div.rankingTableWrapper > table > tbody > tr:nth-child(" + str(num) + ") > td:nth-child(2) > a")

# 値下がり率 1-50位
#    codes = soup.select("#contents-body-bottom > div.rankdata > div.rankingTableWrapper > table > tbody > tr:nth-child(" + str(num) + ") > td:nth-child(2) > a")

# 出来高 1-50位
#    codes = soup.select("#contents-body-bottom > div.rankdata > div.rankingTableWrapper > table > tbody > tr:nth-child(" + str(num) + ") > td:nth-child(2) > a")

    if len(codes) == 0:
        break
    num += 1
    for code in codes:
        l.append(code.text)


# 配列から銘柄名紐づけ

base_url = "https://kabutan.jp/stock/?code="
num = 0
for i in l:
    url = base_url + str(l[num])
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    titles = soup.select("#kobetsu_right > div.company_block > h3")

    num += 1
    for title in titles:
        t.append(title.text)

# csvへ出力

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, lineterminator='\n')
    for row in zip(l, t):
        writer.writerow(row)
