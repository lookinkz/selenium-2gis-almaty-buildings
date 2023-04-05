# get the imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
import re
import csv
from csv_to_list import get_coordinate

coordinates = get_coordinate('almaly-result.csv')
links = list()


def searching(address):
    pass


for coordinate in coordinates:
    street = coordinate[0]
    latitude = coordinate[1]
    longitude = coordinate[2]
    options = Options()
    options.binary_location = r'C:\Users\User\AppData\Local\Mozilla Firefox\firefox.exe'
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    get_url = "https://www.google.com/maps/d/u/0/edit?mid=1aa8HI0f54ijvMbF6Tm7yV5DPE5bFV3U&usp=sharing"
    driver.get(get_url)
    time.sleep(45)

    driver.quit()
