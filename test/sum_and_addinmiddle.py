nums = [5, 25, 10, 35, 20, 45, 30]


def add_in_middle(nums):
    if len(nums) <= 1:
        return nums
    i = 0
    while i < len(nums) - 1:
        temp = nums[i] + nums[i+1]
        nums.insert(i+1, temp)
        i += 2
    return nums


def powerof(val):
    temp = val / 2
    if temp == 2:
        return True
    if not temp == int(temp):
        return False
    return powerof(temp)


print(powerof(512))
