def twoSum(nums: list, target: int) -> list:

    dt = {}
    for i in range(len(nums)):
        try:
            print('curr ele', nums[i])
            if target - nums[i] in dt:
                return [i, dt[target - nums[i]]]
        except KeyError:
            print("no key found for", target - nums[i])
            print(dt)
        dt[nums[i]] = i

e = twoSum([2,7,11,15], 9)
print(e)