from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.justdial.com/Aligarh/Restaurant-Collections/AllCategory').text

soup = BeautifulSoup(source, 'lxml')

#first_div = soup.find('div', class_ = 'mlistviewpr')

first_div = soup.find('div', class_='holder')
# sec_div = first_div.find('div', class_="wrapper filter-section")
# thrid_div = sec_div.find('div')
# anchr = thrid_div.find('div', class_ = 'mlistviewpr').a
#name = anchr.find('span', class_ = 'meditle lng_commn').text

print(name)