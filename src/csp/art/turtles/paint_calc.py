"""Program: paint_calc.py - Calculate paint gallons.

Command line usage:

$ python3 paint_calc
<prompts>
returns -

:return: gallons of paint
:rtype: int
"""


def calc(height: int, length: int, windows: int = 0, doors: int = 0):
    """Calculate gallons of paint for a wall, given the number of windows and doors.

    :param height: Height of the wall.
    :param length: Length of the wall.
    :param windows: Number of windows.
    :param doors: Number of doors.
    """
    wall_area = 2 * length * height
    no_paint_area = 20 * doors + 15 * windows
    paint_area = wall_area - no_paint_area
    gallons_of_paint = round((wall_area / 350), 2)
    return {"gallons of paint": gallons_of_paint, "paint_area": paint_area}


if __name__ == "__main__":
    wall_height = int(input("How high is the wall?"))
    wall_length = int(input("How long is the wall?"))
    num_windows = int(input("How many windows are there?"))
    num_doors = int(input("How many doors are there"))
    print(calc(wall_height, wall_length, num_windows, num_doors))
