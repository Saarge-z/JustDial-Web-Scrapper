# JustDial Web_scrapper


# Python Packages

Use pip as a package manager for installing these packages
    
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from bs4 import BeautifulSoup 
    import requests, os
    import time
    import lxml
    import csv
    import traceback
    from PIL import Image
    import pytesseract

The program searches 6 results only, can be changed from line-56 of justdial_scrap.py. Here mention (number of results required + 1) in place of "7" and voila your'e good to go.


# Instalation Requirements

geckodriver
tesseract - Available inside the project folder
            Install it normally and then
                Add its path to the environment variables of your system.
                or write the below mentioned code in top most justdial_scrap.py just after the 10th line.
                    pytesseract.pytesseract.tesseract_cmd = r"here add path of your installed tesseract.exe file"