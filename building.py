# get the imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time, re, csv
from csv_to_list import get_address

addresses = get_address('almaly.csv')
links = list()
def searching(address):
    search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Поиск в 2ГИС"]')
    time.sleep(2)
    search_box.send_keys(address)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    url = driver.current_url
    match = re.search(r"\?m=([\d\.]+%2C[\d\.]+)%2F", url)
    try:
        coordinates_str = match.group(1)
        coordinates = list(map(float, reversed(coordinates_str.split('%2C'))))
        return coordinates
    except:
        with open('log.txt', 'a', newline='', encoding='utf-8') as log_file:
            log_file.write(f"\n\n-----\n!!! Something went wrong with {address}.\n-----\n\n")
    
    # <input type="text" class="_1gvu1zk" placeholder="Поиск в 2ГИС" value="Алматы Шевченко 147Б" spellcheck="false">

links = list()
for address in addresses:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://2gis.kz/almaty")
    time.sleep(3)
    print(address)
    coordinates = searching(address)
    result = [address, coordinates]
    with open('result.csv', 'a', newline='', encoding='utf-8') as result_file:
        writer = csv.writer(result_file)
        writer.writerow(result)
    driver.quit()
    

