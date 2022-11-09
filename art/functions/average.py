"""Program: average.py - Calculate average of a list of numbers.

Command line usage:
$ python3 average.py [7,8,9,10]
8.5

--default prints above test
"""


def average(nums):
    """This function takes a list of numbers and returns the average of.
    """
    total = sum(nums)
    avg = total / len(nums)
    return avg


scores = [7, 8, 9, 10]

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        if "--default" not in sys.argv:
            print(average(sys.argv[1]))
        else:
            print(scores)
            print(average(scores))
    else:
        print(__doc__)
