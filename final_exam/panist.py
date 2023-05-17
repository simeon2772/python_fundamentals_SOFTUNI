number_of_pieces = int(input())
music_pieces = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    music_pieces[piece] = [composer, key]

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in music_pieces:
            print(f"{piece} is already in the collection!")
            continue
        music_pieces[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")

    if command[0] == "Remove":
        piece = command[1]
        if piece not in music_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            continue
        del music_pieces[piece]
        print(f"Successfully removed {piece}!")
    if command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece not in music_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            continue
        music_pieces[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
for k, v in music_pieces.items():
    composer, key = v
    print(f"{k} -> Composer: {composer}, Key: {key}")