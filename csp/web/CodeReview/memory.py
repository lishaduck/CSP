import random
import turtle

#############################
# Set up screen and images
#############################
screen = turtle.Screen()
screen.bgcolor("teal")
face_down = "FaceDown.gif"
screen.register_shape(face_down)
shapes = [
    "Banana",
    "Crocodile",
    "Dolphin",
    "Elephant",
    "Monkey",
    "Queen",
    "Rocket",
    "Volcano",
]
shapes = [f"images/{shape}.gif" for shape in shapes]
for shape in shapes:
    screen.register_shape(shape)


#############################
# Writing functions
#############################


def write_text(message):
    writer.clear()
    writer.write(message, font=("Arial", 36, "normal"))


def write_score():
    scorer.clear()
    scorer.write(f"Score: {score}", font=("Arial", 36, "normal"))


#############################
# Event handlers
#############################


def shuffle_and_reset():
    global score, matched
    score = 0
    matched = 0
    to_check.clear()
    write_score()
    write_text("Click the cards to make a match")
    random.shuffle(answers)
    for card in cards:
        card.shape(face_down)
        card.showturtle()


def check_card(index):
    if len(to_check) < 2:
        card = cards[index]
        if card.shape() == face_down:
            card.shape(answers[index])
            to_check.append(index)
            if len(to_check) == 2:
                screen.ontimer(check_for_match, 1000)


def check_for_match():
    global score, matched
    index1 = to_check[0]
    index2 = to_check[1]
    score += 1
    write_score()
    if answers[index1] == answers[index2]:
        cards[index1].hideturtle()
        cards[index2].hideturtle()
        matched += 1
        if matched == 8:
            write_text("You won! Press s to restart.")
    else:
        cards[index1].shape(face_down)
        cards[index2].shape(face_down)

    to_check.clear()


#############################
# Global Variables
#############################

score = 0
matched = 0
to_check = []
cards = []
answers = []

for shape in shapes:
    answers.append(shape)
    answers.append(shape)

#############################
# Writing turtles
#############################

writer = turtle.Turtle()
writer.penup()
writer.goto(-225, 325)
writer.color("white")
writer.hideturtle()
write_text("Press s to get started!")


scorer = turtle.Turtle()
scorer.penup()
scorer.goto(-225, -350)
scorer.hideturtle()
scorer.color("white")


#############################
# Set up Board
#############################
index = 0
for y in [225, 75, -75, -225]:
    for x in [-225, -75, 75, 225]:
        t = turtle.Turtle()
        t.shape(shapes[index % len(shapes)])
        t.speed(0)
        t.penup()
        t.goto(x, y)
        t.onclick(lambda x, y, i=index: check_card(i))
        cards.append(t)
        index += 1
        print(f"creating turtle at ({x},{y})")


#############################
# Start Game
#############################

screen.onkeypress(shuffle_and_reset, "s")
screen.listen()
screen.mainloop()
