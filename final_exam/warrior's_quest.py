skill = input()

while True:
    command = input().split()
    if " ".join(command[0:2]) == "For Azeroth":
        break
    if command[0] == "GladiatorStance":
        for letters in skill:
            upper_letters = letters.upper()
            print(upper_letters, end="")
    if command[0] == "DefensiveStance":
        for letters in skill:
            lower_letters = letters.lower()
            print(lower_letters, end="")
    if command[0] == "Dispel":
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(skill):
            skill = skill[:index] + letter + skill[index + 1:]
            print("Success!")
        else:
            print("Dispel too weak.")
    if command[0] == "Target":
        if command[1] == "Change":
            first_substring = command[2]
            second_substring = command[3]
            if first_substring in skill:
                skill.replace(first_substring, second_substring)
                print(skill)
            else:
                print(skill)
        elif command[1] == "Remove":
            substring = command[2]
            if substring in skill:
                skill.replace(substring, " ")
                print(skill)
            else:
                continue

