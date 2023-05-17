concert = {}
playtime_concert = {}
while True:
    command = input().split("; ")
    if command[0] == "Start!":
        break
    elif command[0] == "Add":
        band_name = command[1]
        members = command[2].split(", ")
        if band_name not in concert.keys():
            concert[band_name] = 0
            concert[band_name] = members
        if members not in concert.values():
            concert[band_name] += members

    elif command[0] == "Play":
        band_name = command[1]
        time = int(command[2])
        if band_name in playtime_concert.keys():
            playtime_concert[band_name] += time
        if band_name not in playtime_concert.keys():
            playtime_concert[band_name] = 0
            playtime_concert[band_name] = time
print(f"Total time: {sum(playtime_concert.values())}")
for band_name, time in playtime_concert.items():
    print(f"{band_name} -> {time}")
print("".join(concert.keys()))
for member in concert.values():
    print(f"=> {' '.join(member)}")
