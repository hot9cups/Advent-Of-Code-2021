def getPowerConsumption2(codes):
    gamma, epsilon = ["0"] * len(codes[0]), ["0"] * len(codes[0])

    for i in range(len(codes[0])):
        one_count = 0
        for code in codes:
            if code[i] == "1":
                one_count += 1
        if one_count >= (len(codes) // 2):
            gamma[i] = "1"
        else:
            epsilon[i] = "1"
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def getPowerConsumpution(codes):
    num_bits = len(codes[0])
    gamma, epsilon = 0, 0

    for bit_len in range(num_bits):
        mask = 1 << bit_len
        one_count = 0
        for code in codes:
            one_count += 1 if (mask & int(code, 2)) != 0 else 0
        if one_count >= (len(codes) // 2):
            gamma |= mask
        else:
            epsilon |= mask

    return gamma * epsilon


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
print(getPowerConsumption2(codes))

with open("data.txt") as f:
    codes = [code.strip() for code in f.readlines()]
# The bloody strip() got me, dammit

print(getPowerConsumpution(codes))
print(getPowerConsumption2(codes))
