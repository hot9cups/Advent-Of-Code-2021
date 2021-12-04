def getPos(moves):
    x, y = 0, 0
    mapping = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}

    for move in moves:
        delta = mapping[move[0]]
        x += delta[0] * move[1]
        y += delta[1] * move[1]
    return x * y


moves = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
moves = [(item.split()[0], int(item.split()[1])) for item in moves]

print(getPos(moves))

with open("data.txt") as f:
    moves = [line.split() for line in f.readlines()]
    moves = [(item[0], int(item[1])) for item in moves]

print(getPos(moves))
