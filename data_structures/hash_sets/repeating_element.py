
def repeating_elements(nums):
    seen = set()
    repeated = set()

    for item in nums:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)

    repeated_list = list(repeated)
    return repeated_list



print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []