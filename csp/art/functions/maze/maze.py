""""""


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
    maze_painter.forward((path_width + (iteration * 10)) / 10)
    if rand.randint(1, 10) > 7:
        draw_barrier()


def draw_barrier():
    maze_painter.left(90)
    maze_painter.forward(path_width)
    maze_painter.right(180)
    maze_painter.forward(path_width)
    maze_painter.left(90)


def draw_door():
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()


def draw_maze() -> None:
    """Draw the maze.

    Lines are drawn in the turtle window.

    param maze: the maze as a list of lists of lines
    """
    for i in range(num_walls):
        door_spacer = 0
        maze_painter.forward(path_width / 4)
        for j in range(5):
            options: int = rand.randint(1, 10)
            maze_painter.forward((i + path_width) / 10)
            if options > 3 and door_spacer == 0:
                draw_door()
                door_spacer += 1
            else:
                draw_wall(i)
            maze_painter.forward(40)
            if i > 4:
                draw_barrier()
            maze_painter.forward((i + path_width) / 10)
        maze_painter.forward((path_width / 4) + i)
        maze_painter.left(90)


def go_up():
    maze_runner.setheading(90)
    maze_runner.forward(20)


def go_down():
    maze_runner.setheading(270)
    maze_runner.forward(20)


def go_left():
    maze_runner.setheading(180)
    maze_runner.forward(20)


def go_right():
    maze_runner.setheading(0)
    maze_runner.forward(20)


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
    wn.listen()

    draw_maze()

    wn.mainloop()
