def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return "No second largest number."

    return unique[-2]

nums = [10, 25, 40, 30, 40, 15]
print("Second Largest:", second_largest(nums))
