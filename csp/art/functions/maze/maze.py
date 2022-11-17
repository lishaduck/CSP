"""Maze - Play a maze game.

Have fun!
"""


import random as rand
import turtle as trtl

from csp.utilities import COLORS, TURTLE_SHAPES, artistic_text

# -----game configuration----
num_walls = 26
wall_color = "black"
wall_width = 5
path_width = 20
turtle_speed = 0


# -----game functions-----
def draw_wall(iteration):
    """Draw a blank wall segment."""
    maze_painter.forward(((path_width / 10) + (iteration * 10)) / 4)


def draw_barrier(iteration):
    """Draw a barrier, then draw a wall segment."""
    maze_painter.left(90)
    maze_painter.forward(path_width)
    maze_painter.right(180)
    maze_painter.forward(path_width)
    maze_painter.left(90)
    draw_wall(iteration)


def draw_door(iteration):
    """Draw a door, then draw a wall segment."""
    maze_painter.penup()
    draw_wall(iteration)
    maze_painter.pendown()


def draw_maze() -> None:
    """Draw the maze.

    Lines are drawn in the turtle window.

    param maze: the maze as a list of lists of lines
    """
    for i in range(num_walls):
        door_spacer = 0
        for j in range(5):
            draw_wall(i)
            if rand.randint(1, 10) > 3:
                draw_door(i)
                door_spacer += 1
            else:
                draw_wall(i)
            if (i >= 1) and (rand.randint(1, 10) > 7):
                draw_barrier(i)
            draw_wall(i)
        if door_spacer == 0:
            draw_door(i)
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
