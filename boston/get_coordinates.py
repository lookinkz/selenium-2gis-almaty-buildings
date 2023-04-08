# get the imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import csv


def get_links(f):
    print(f"Getting the addresses and converting in to the list from {f}")
    addresses = list()
    links = list()
    with open(f, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            address = row[0]
            addresses.append(address)
            link = row[1]
            links.append(link)

    print("Success! The list of addresses are ready.\n\n")
    return (addresses, links)


csvfile = 'gis_links.csv'
addresses, links = get_links(csvfile)
i = 0
for link in links:
    print(addresses[i], links[i])
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    time.sleep(2)
    url = driver.current_url
    match = re.search(r"\?m=([\d\.]+%2C[\d\.]+)%2F", url)
    try:
        coordinates_str = match.group(1)
        coordinates = list(map(float, reversed(coordinates_str.split('%2C'))))
        print(addresses[i], links[i], coordinates)
        row = [addresses[i], links[i], coordinates]
        with open('gis_links_coordinates.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(row)
    except:
        with open('log.txt', 'a', newline='', encoding='utf-8') as log_file:
            log_file.write(
                f"\n\n-----\n!!! Something went wrong with {addresses[i]}.\n-----\n\n")
    i += 1


# links = list()
# for address in addresses:
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.get("https://2gis.kz/almaty")
#     time.sleep(3)
#     print(address)
#     coordinates = searching(address)
#     result = [address, coordinates]
#     with open('result.csv', 'a', newline='', encoding='utf-8') as result_file:
#         writer = csv.writer(result_file)
#         writer.writerow(result)
#     driver.quit()
