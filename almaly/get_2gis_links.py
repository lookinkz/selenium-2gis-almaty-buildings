# get the imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time, re, csv, pyperclip
from boston.csv_to_list import get_coordinate

addresses = get_coordinate('2gis_links.csv')
print(addresses)

def searching(address):
    search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Поиск в 2ГИС"]')
    time.sleep(2)
    search_box.send_keys(address)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)    
    try:
        send_button = driver.find_element(By.XPATH, "//span[text()='Отправить']/parent::button")
        send_button.click()
        time.sleep(2)
        copy_button = driver.find_element(By.XPATH, "//div[@class='_qkzbgc']//button[text()='Скопировать']")
        copy_button.click()
        link = pyperclip.paste()
        row = [address, link]
    except:
        row = "No link"
    return(row)

    
for address in addresses:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://2gis.kz/almaty")
    time.sleep(3)
    row = searching(address)
    print(row)
    with open('addresses_with_2gis.csv', 'a', newline='', encoding='utf-8') as result_file:
        writer = csv.writer(result_file)
        writer.writerow(row)
        
        
