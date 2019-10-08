from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.justdial.com/Delhi/Ardor-Restaurant-Lounge-Terrace-Cafe-Connaught-Place/011PXX11-XX11-121106171304-R3S5_BZDET?srcterm=Ardor%2520Restaurant%2520Lounge%2520Terrace%2520Cafe'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req)

soup = BeautifulSoup(webpage)
print(soup)



#first_div = soup.find('div', class_ = 'mlistviewpr')

#first_div = soup.find('div', class_='holder')
# sec_div = first_div.find('div', class_="wrapper filter-section")
# thrid_div = sec_div.find('div')
# anchr = thrid_div.find('div', class_ = 'mlistviewpr').a
#name = anchr.find('span', class_ = 'meditle lng_commn').text

#print(name)