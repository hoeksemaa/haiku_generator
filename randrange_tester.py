from random import randrange

nums = [[], [], []]
for i in range(30):
    nums[0].append(randrange(3))
    nums[1].append(randrange(1, 3))
    nums[2].append(randrange(0, 3))

for i in range(len(nums)):
    print("{}: {}".format(i, " ".join(map(str, nums[i]))))
