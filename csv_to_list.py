import csv

def get_address(f):
    print(f"Getting the addresses and converting in to the list from {f}")
    addresses = list()
    with open(f, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            street = row[0]
            num = row[1]
            num = "".join(num.split())
            address = f"Алматы {street} {num}"
            addresses.append(address)

    print("Success! The list of addresses are ready.\n\n")
    return(addresses)