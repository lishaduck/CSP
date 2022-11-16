""""""

# import random as rand
import turtle as trtl

from csp.utilities import artistic_text

# -----game configuration----
num_walls = 26
wall_color = "black"
wall_width = 5
path_width = 20
turtle_speed = 0


def draw_wall():
    maze_painter.left(90)
    maze_painter.forward(path_width)
    maze_painter.right(180)
    maze_painter.forward(path_width)
    maze_painter.left(90)


def draw_maze() -> None:
    """Draw the maze.

    Lines are drawn in the turtle window.

    param maze: the maze as a list of lists of lines
    """
    for i in range(num_walls):
        maze_painter.forward(i + path_width)
        maze_painter.penup()
        maze_painter.forward(path_width)
        maze_painter.pendown()
        maze_painter.forward(40)
        if i > 4:
            draw_wall()
        maze_painter.forward(9 * i + path_width)

        maze_painter.left(90)


# main entrypoint
if __name__ == "__main__":
    artistic_text("MAZE", speed=0.02, font="tarty-9")

    maze_painter = trtl.Turtle()
    maze_painter.speed(turtle_speed)
    maze_painter.pencolor(wall_color)
    maze_painter.pensize(wall_width)

    wn = trtl.Screen()
    wn.bgcolor("white")

    # get the maze
    # maze = get_maze()
    # get the start and end points
    # start, end = get_start_end(maze)
    # print the path
    draw_maze()
    wn.mainloop()
