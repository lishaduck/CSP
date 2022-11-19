"""Maze - Play a maze game.

Have fun!
"""


import random as rand
import turtle as trtl

from csp.utilities import COLORS, TURTLE_SHAPES, artistic_text

# -----game configuration----
num_walls = 25
wall_color = rand.choice(COLORS)
wall_width = 5
path_width = 15
turtle_speed = 0


# def wall_length(iteration):
#     length = (iteration * 10) * (path_width / 100)
#     return length


# -----game functions-----


def draw_wall(door, barrier, wall_len):
    """Draw a blank wall segment."""
    if door < barrier:
        draw_door(door)
        draw_barrier(barrier - door - path_width * 2)
        # draw the rest of the wall
        maze_painter.forward(wall_len - barrier)
    else:
        draw_barrier(barrier)
        draw_door(door - barrier)
        # draw the rest of the wall
        maze_painter.forward(wall_len - door - path_width * 2)
    maze_painter.left(90)


def draw_barrier(pos):
    """Draw a barrier, then draw a wall segment."""
    maze_painter.forward(pos)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.backward(path_width * 2)
    maze_painter.right(90)


def draw_door(pos):
    """Draw a door, then draw a wall segment."""
    maze_painter.forward(pos)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()


def draw_maze() -> None:
    """Draw the maze.

    Lines are drawn in the turtle window.

    param maze: the maze as a list of lists of lines
    """
    wall_len = path_width
    for i in range(num_walls):
        wall_len += path_width
        if i > 4:

            # randomize location of doors and barriers in wall
            door = rand.randint(path_width * 2, (wall_len - path_width * 2))
            barrier = rand.randint(path_width * 2, (wall_len - path_width * 2))
            # if a door and barrier would be rendered on top of each other, get a new value
            while abs(door - barrier) < path_width:
                door = rand.randint(path_width * 2, (wall_len - path_width * 2))

            draw_wall(door, barrier, wall_len)
        else:
            maze_painter.forward(wall_len)
            maze_painter.left(90)


def go_up():
    """Orient the runner up."""
    maze_runner.setheading(90)


def go_down():
    """Orient the runner down."""
    maze_runner.setheading(270)


def go_left():
    """Orient the runner left."""
    maze_runner.setheading(180)


def go_right():
    """Orient the runner right."""
    maze_runner.setheading(0)


def move_runner():
    """Move the runner forward in the selected direction."""
    maze_runner.forward(5)


# main entrypoint
if __name__ == "__main__":
    artistic_text("MAZE", speed=0.001, font="tarty-9")

    maze_painter = trtl.Turtle()
    maze_painter.speed(turtle_speed)
    maze_painter.pencolor(wall_color)
    maze_painter.pensize(wall_width)

    maze_runner = trtl.Turtle()
    maze_runner.shape(rand.choice(TURTLE_SHAPES))
    maze_runner.color(rand.choice(COLORS))

    wn = trtl.Screen()
    wn.bgcolor("white")

    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")
    wn.onkeypress(move_runner, "g")
    wn.listen()

    draw_maze()

    wn.mainloop()
