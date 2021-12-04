def getPowerConsumpution(codes):
    return 0


codes = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

print(getPowerConsumpution(codes))

with open("data.txt") as f:
    codes = [code for code in f.readlines()]

print(getPowerConsumpution(codes))
