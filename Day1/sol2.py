def getTimesIncreases(nums):
    total = nums[0] + nums[1] + nums[2]
    count = 0

    for i in range(3, len(nums)):
        curr_total = total - nums[i - 3] + nums[i]
        count += 1 if curr_total > total else 0
        total = curr_total
    return count


# nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# print(getTimesIncreases(nums))

with open("data.txt") as f:
    nums = [int(num) for num in f.readlines()]
print(getTimesIncreases(nums))
