import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {'Name': [], 'Price': []}

url='https://finance.yahoo.com/screener/predefined/ms_basic_materials/'
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=headers)
soup= BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())

spans = soup.find_all('td', {'class': 'Va(m) Ta(start) Px(10px) Fz(s)'})
#<td colspan="" class="Va(m) Ta(start) Px(10px) Fz(s)" aria-label="Name">Nucor Corporation</td>

prices = soup.find_all('td', {'class': 'Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)', 'aria-label': 'Price (Intraday)'})

#<td colspan="" class="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)" aria-label="Price (Intraday)"><fin-streamer data-test="colorChange" class="" data-symbol="BHP" data-field="regularMarketPrice" data-trend="none" data-pricehint="2" value="55.4" active="">55.40</fin-streamer></td>

# print(spans)

for span in spans:
    print(span.text)
    data['Name'].append(span.text)

for price in prices:
    print(price.text)
    data['Price'].append(price.text)
    

df = pd.DataFrame.from_dict(data)
df.to_csv("data1.csv", index=False)