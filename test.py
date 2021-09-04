import time

curr = time.time()

def twoSum(nums, target):
        for x in range(len(nums)):
            ans = target - nums[x]
            if ans in nums[x+1:]:
                return [x, (nums[x+1:].index(ans) + (x+1))]
        return None

curr = time.time() - curr

print(twoSum([3,2,95,4,-3], 92))
print(curr)