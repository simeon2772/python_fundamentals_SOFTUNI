band_info = {}
band_play_time = {}

while True:
    command = input().split("; ")
    if command[0] == "Start!":
        break

    if command[0] == "Add":
        band_name = command[1]
        band_members = command[2].split(", ")
        if band_name not in band_info:
            band_info[band_name] = band_members
            continue
        for member in band_members:
            if member not in band_info[band_name]:
                band_info[band_name].append(member)

    elif command[0] == "Play":
        band_name = command[1]
        play_time = int(command[2])
        if band_name not in band_play_time:
            band_play_time[band_name] = play_time
            continue
        band_play_time[band_name] += play_time

total_time = sum(band_play_time.values())

print(f"Total time: {total_time}")
for name, time in band_play_time.items():
    print(f"{name} -> {time}")

band, members = next(iter(band_info.items()))

print(f"{band}")
for member in members:
    print(f"=> {member}")

