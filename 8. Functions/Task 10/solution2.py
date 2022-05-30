from functools import reduce
def sum_digits(nums):
    result = reduce(lambda x, y: int(x) + int(y), str(nums))
    return result
print(sum_digits(105))

