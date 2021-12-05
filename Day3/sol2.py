def filterDown(codes, pos, keep_ones):
    one_count, mask, half_len = 0, 1 << pos, (len(codes) + 1) // 2
    for code in codes:
        if (int(code, 2) & mask) != 0:
            one_count += 1

    majority = (
        mask
        if (one_count >= half_len and keep_ones)
        or (not keep_ones and one_count < half_len)
        else 0
    )
    res = [code for code in codes if (int(code, 2) & mask) == majority]
    return res


def diagnose(codes, forOxygen):
    pos = 1
    while len(codes) != 1:
        codes = filterDown(codes, len(codes[0]) - pos, forOxygen)
        pos += 1
    return codes[0]


def getOxygenAndCO2(codes):
    return diagnose(codes, True), diagnose(codes, False)


def getLifeSupportRating(codes):
    oxygen_generator, co2_scrubber = getOxygenAndCO2(codes)
    return int(oxygen_generator, 2) * int(co2_scrubber, 2)


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

print(getLifeSupportRating(codes))

with open("data.txt") as f:
    codes = [code.strip() for code in f.readlines()]
# The bloody strip() got me, dammit

print(getLifeSupportRating(codes))
