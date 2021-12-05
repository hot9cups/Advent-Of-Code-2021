import pprint


def finalScore(board, seen, last_number):
    total = 0
    for row in board:
        for num in row:
            if num not in seen:
                total += num
    return total * last_number


def getFirstWinnerScore(numbers, boards, num2board):
    seen = set()
    rowsDone, colsDone = {}, {}
    for number in numbers:
        seen.add(number)
        for entry in num2board.get(number, []):
            boardIdx, row, col = entry
            rowsDone.setdefault(boardIdx, {})[row] = (
                rowsDone.get(boardIdx, {}).get(row, 0) + 1
            )
            colsDone.setdefault(boardIdx, {})[col] = (
                colsDone.get(boardIdx, {}).get(col, 0) + 1
            )
            if rowsDone[boardIdx][row] == 5 or colsDone[boardIdx][col] == 5:
                return finalScore(boards[boardIdx], seen, number)
    return 0


def parseInput(data):
    numbers, boards, num2board = [int(num) for num in data[0].split(",")], [], {}
    for i in range(2, len(data), 6):
        board = []
        for j in range(5):
            row = list(map(int, data[i + j].split()))
            for idx, num in enumerate(row):
                num2board.setdefault(num, []).append((len(boards), j, idx))
            board.append(row)
        boards.append(board)
    return numbers, boards, num2board


with open("demo_data.txt") as f:
    data = f.readlines()
    numbers, boards, num2board = parseInput(data)
    # print(numbers)
    # pprint.pprint(boards)

print(getFirstWinnerScore(numbers, boards, num2board))

with open("data.txt") as f:
    data = f.readlines()
    numbers, boards, num2board = parseInput(data)

print(getFirstWinnerScore(numbers, boards, num2board))
