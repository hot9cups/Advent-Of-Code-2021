def getPos(moves):
    x, y, aim = 0, 0, 0
    mapping = {"down": 1, "up": -1}

    for move in moves:
        if move[0] == "forward":
            x += move[1]
            y += aim * move[1]
        else:
            aim += mapping[move[0]] * move[1]
    return x * y


moves = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
moves = [(item.split()[0], int(item.split()[1])) for item in moves]

print(getPos(moves))

with open("data.txt") as f:
    moves = [line.split() for line in f.readlines()]
    moves = [(item[0], int(item[1])) for item in moves]

print(getPos(moves))
