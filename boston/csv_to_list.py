import csv
import re


def get_address(f):
    print(f"Getting the addresses and converting in to the list from {f}")
    addresses = list()
    with open(f, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            address = row[0]
            addresses.append(address)

    print("Success! The list of addresses are ready.\n\n")
    return (addresses)
