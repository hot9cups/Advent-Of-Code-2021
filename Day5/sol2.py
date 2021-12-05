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


def populateDiagTopToBottom(board):
    rows, cols = len(board), len(board[0])
    for i in range(rows - 1, -1, -1):
        runSum = 0
        j = 0
        while i < rows and j < cols:
            runSum += board[i][j][3]
            board[i][j][2] += runSum
            i, j = i + 1, j + 1

    for j in range(1, cols):
        runSum = 0
        i = 0
        while i < rows and j < cols:
            runSum += board[i][j][3]
            board[i][j][2] += runSum
            i, j = i + 1, j + 1


def populateDiagBottomToTop(board):
    rows, cols = len(board), len(board[0])
    for j in range(cols - 1, -1, -1):
        runSum = 0
        i = rows - 1
        while i >= 0 and j < cols:
            runSum += board[i][j][4]
            board[i][j][2] += runSum
            i, j = i - 1, j + 1

    for i in range(rows - 2, -1, -1):
        runSum = 0
        j = 0
        while i >= 0 and j < cols:
            runSum += board[i][j][4]
            board[i][j][2] += runSum
            i, j = i - 1, j + 1


def populate(board):
    populateHorizontal(board)
    populateVertical(board)
    populateDiagTopToBottom(board)
    populateDiagBottomToTop(board)


def countAllCrossovers(lines, rows, cols):
    board = [[[0, 0, 0, 0, 0] for _ in range(rows)] for _ in range(cols)]
    # [vertical, horizontal, value, diagTtB, diagBtT]
    for line in lines:
        (x1, y1), (x2, y2) = line
        if y1 == y2:
            board[x1][y1][0] += 1
            board[x2 + 1][y1][0] -= 1
        elif x1 == x2:
            board[x1][y1][1] += 1
            board[x1][y2 + 1][1] -= 1
        elif y1 < y2:
            board[x1][y1][3] += 1
            board[x2 + 1][y2 + 1][3] -= 1
        elif y1 > y2:
            board[x2][y2][4] += 1
            board[x1 - 1][y1 + 1][4] -= 1

    populate(board)
    return sum(sum(1 for item in row if item[2] > 1) for row in board)


def parseInput(data):
    lines = []
    rows, cols = 0, 0
    for line in data:
        line = line.strip().split(" -> ")
        x1, y1 = map(int, line[0].strip().split(","))
        x2, y2 = map(int, line[1].strip().split(","))
        lines.append(sorted([(x1 + 1, y1 + 1), (x2 + 1, y2 + 1)]))
        rows = max(rows, x1 + 1, x2 + 1)
        cols = max(cols, y1 + 1, y2 + 1)
    return lines, rows + 10, cols + 10


with open("demo_data.txt") as f:
    data = f.readlines()
    lines, rows, cols = parseInput(data)

print(countAllCrossovers(lines, rows, cols))

with open("data.txt") as f:
    data = f.readlines()
    lines, rows, cols = parseInput(data)

print(countAllCrossovers(lines, rows, cols))
