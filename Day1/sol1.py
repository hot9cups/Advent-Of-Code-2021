def getTimesIncrease(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    return count


# nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# print(getTimesIncreases(nums))

with open("data.txt") as f:
    nums = [int(num) for num in f.readlines()]

print(getTimesIncrease(nums))
