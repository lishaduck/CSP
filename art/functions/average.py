"""Program: average.py - calculate average of a list of numbers.
"""


def average(nums):
    total = sum(nums)
    avg = total / len(nums)
    return avg


scores = [7, 8, 9, 10]
print(average(scores))
