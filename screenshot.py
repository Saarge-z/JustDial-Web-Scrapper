from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium"
driver = webdriver.Firefox()

url = 'https://www.justdial.com/Delhi/Ardor-Restaurant-Lounge-Terrace-Cafe-Connaught-Place/011PXX11-XX11-121106171304-R3S5_BZDET?srcterm=Ardor%2520Restaurant%2520Lounge%2520Terrace%2520Cafe'
driver.get(url)
driver.save_screenshot("screenshot.png")
print (driver.title)
driver.close()