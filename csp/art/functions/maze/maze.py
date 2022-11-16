""""""

# import random as rand
import turtle as trtl

from csp.utilities import artistic_text

# -----game configuration----
num_walls = 26
wall_color = "black"
wall_width = 5
path_width = 10


maze_painter = trtl.Turtle()
maze_painter.pencolor(wall_color)
maze_painter.pensize(wall_width)

wn = trtl.Screen()
wn.bgcolor("white")

Maze_Input = list[list[int]]


def get_maze() -> Maze_Input:
    """Randomly generate a maze.

    :return: the maze as a list of lists of lines
    """
    return Maze_Input()


def get_start_end(maze) -> tuple[tuple[int, int], tuple[int, int]]:
    """Get the start and end positions.

    :param maze: the maze as a list of lists of lines
    :return: the start and end positions as tuples
    """
    return ((0, 0), (0, 0))


def draw_maze(maze: Maze_Input, start, end) -> None:
    """Draw the maze.

    Lines are drawn in the turtle window.

    :param maze: the maze as a list of lists of lines
    """
    for i in range(num_walls):
        maze_painter.forward(i * 10)
        maze_painter.left(90)


# main entrypoint
if __name__ == "__main__":
    artistic_text("MAZE", speed=0.05)

    # get the maze
    maze = get_maze()
    # get the start and end points
    start, end = get_start_end(maze)
    # print the path
    draw_maze(maze, start, end)
    wn.mainloop()
