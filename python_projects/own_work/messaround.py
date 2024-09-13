import bs4, os, requests

res = requests.get('https://www.timeanddate.com/weather/egypt/cairo/ext')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

temp = soup.select('.temp')

print(len(temp))