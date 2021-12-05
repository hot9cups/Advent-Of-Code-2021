def populateHorizontal(board):
    rows, cols = len(board), len(board[0])
    for i in range(rows):
        runSum = 0
        for j in range(cols):
            runSum += board[i][j][1]
            board[i][j][2] += runSum


def populateVertical(board):
    rows, cols = len(board), len(board[0])
    for j in range(cols):
        runSum = 0
        for i in range(rows):
            runSum += board[i][j][0]
            board[i][j][2] += runSum


def populate(board):
    populateHorizontal(board)
    populateVertical(board)


def countHorizontalAndVerticalCrossovers(lines, rows, cols):
    board = [[[0, 0, 0] for _ in range(rows)] for _ in range(cols)]

    for line in lines:
        (x1, y1), (x2, y2) = line
        if y1 == y2:
            board[x1][y1][0] += 1
            board[x2 + 1][y1][0] -= 1
        elif x1 == x2:
            board[x1][y1][1] += 1
            board[x1][y2 + 1][1] -= 1

    populate(board)
    return sum(sum(1 for item in row if item[2] > 1) for row in board)


def parseInput(data):
    lines = []
    rows, cols = 0, 0
    for line in data:
        line = line.strip().split(" -> ")
        x1, y1 = map(int, line[0].strip().split(","))
        x2, y2 = map(int, line[1].strip().split(","))
        lines.append(sorted([(x1, y1), (x2, y2)]))
        rows = max(rows, x1, x2)
        cols = max(cols, y1, y2)
    return lines, rows + 2, cols + 2


with open("demo_data.txt") as f:
    data = f.readlines()
    lines, rows, cols = parseInput(data)

print(countHorizontalAndVerticalCrossovers(lines, rows, cols))

with open("data.txt") as f:
    data = f.readlines()
    lines, rows, cols = parseInput(data)

print(countHorizontalAndVerticalCrossovers(lines, rows, cols))
