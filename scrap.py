from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.justdial.com/Delhi/Ardor-Restaurant-Lounge-Terrace-Cafe-Connaught-Place/011PXX11-XX11-121106171304-R3S5_BZDET?srcterm=Ardor%2520Restaurant%2520Lounge%2520Terrace%2520Cafe'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req)

soup = BeautifulSoup(webpage, 'lxml')



first_div = soup.find('div', class_ = 'mlistviewpr')

first_div = soup.find('div', class_='holder')
#sec_div = first_div.find('div', class_="wrapper filter-section")
sec_div = first_div.find('div', class_='col-sm-12 col-xs-12 padding0 paddingR0')
thrid_div = sec_div.find('ul', class_='comp-contact')
# anchr = thrid_div.find('ul', class_ = 'ic_phn comp-icon')
# name = anchr.a.text
frth = thrid_div.find('span', class_='telnowpr')
name = frth.find('a', class_='tel ttel')

print(name)