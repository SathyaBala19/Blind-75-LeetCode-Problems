def two_sum(nums, target):
    hash_map = {}

    for i in range(len(nums)):
        current = nums[i]

        needed = target - current

        if needed in hash_map:
            return [hash_map[needed], i]
        
        hash_map[current] = i

nums = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the Target element: "))

result = two_sum(nums, target)

print(result)