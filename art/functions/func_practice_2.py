"""Program: func_practice_2.py - calculate numbers.
"""


def triple(num):
    """Triple a number."""
    return num * 3


def triangle_area(base, height):
    """Calculate the angle of a triangle given the base and the height."""
    area = 1 / 2 * base * height
    return area


def min_val(num1, num2):
    """Return the lower of two numbers."""
    if num1 <= num2:
        return num1
    return num2


# print "The min is 10"
X = min_val(10, 14)
print("The min is " + str(X))
