def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second, first = first, n
        elif first > n > second:
            second = n
    return second

nums = [12, 45, 23, 67, 45, 89]
print("Second Largest:", second_largest(nums))
