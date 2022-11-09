"""Program: schedule.py - check your (hardcoded) calendar."""


# Write a program to check your daily schedule:
# M/W: set your alarm for 7:30am, you have practice and coding class and no time to go to the gym
# T/R: set your alarm for 7:30am, you have no practice or class but can go to the gym
# F: set your alarm for 6:30am, you have practice but no time for class or gym
# S/U: no alarm, no practice, no class, but lots of time for the gym


print("Enter days of the week as MTWRFSU")
DAY = input("Enter a day of the week: ")
if DAY in ("M", "m", "W", "m"):
    ALARM = "7:30"
    CODING_CLASS = True
    PRACTICE = True
    GYM = False
    WORK = False
elif DAY in ("T", "t", "R", "r"):
    ALARM = "7:30"
    CODING_CLASS = False
    PRACTICE = False
    GYM = "Depends"
    WORK = False
elif DAY in ("F", "f"):
    ALARM = "6:30"
    CODING_CLASS = False
    PRACTICE = True
    GYM = False
    WORK = "Depends"
elif DAY in ("S", "s", "U", "u"):
    ALARM = False
    CODING_CLASS = False
    PRACTICE = False
    GYM = True
    WORK = "Depends"
else:
    ALARM = False
    CODING_CLASS = False
    PRACTICE = False
    GYM = False
    WORK = False

if DAY not in ("M", "T", "W", "R", "F", "S", "U", "m", "t", "w", "r", "f", "s", "u"):
    print("That's not an option. Oh well ...")

print(
    "Today is",
    DAY,
    "alarm:",
    ALARM,
    "class:",
    CODING_CLASS,
    "practice:",
    PRACTICE,
    "work:",
    WORK,
)
