
nums_ = [2,7,11,15]

target_ = 9

def twoSum(nums,target):
    from itertools import combinations
    for pair in combinations(nums,2):
        if sum(pair) == target:
            return pair
    return None

ret = twoSum(nums_,target_)

assert twoSum(nums_,target_) == (1,7)