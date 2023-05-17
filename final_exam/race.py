import re

while True:
    text = input()
    matches = re.findall(r"([#$%*&])([A-Za-z]+)\1=(\d+)!!(.+)$", text)
    if matches:
        for match in matches:
            driver_name = match[1]
            length_of_code = int(match[2])
            geohash_code = match[3]
        print(f"Coordinates found! {driver_name} -> {geohash_code}")
        break
    else:
        print("Nothing found!")
    for match in matches:
        driver_name = match[1]
        length_of_code = match[2]
        geohash_code = match[3]
