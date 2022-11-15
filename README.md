# CSP

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)][black] [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)][pylint] [![testing: pytest](https://img.shields.io/badge/testing-pytest-orange)][pytest]

This repo tracks my progress in [Advanced Placement][ap] [Project Lead the Way][pltw] [Computer Science Principles][csp], the second class in the [Project Lead the Way Computer Science][pltw csp] classes.

## Organization

This repo is roughly organized by unit:

-   ### [`art`](/csp/art/) is unit 1: Creative Computing for All

    -   [`turtles`][turtles folder] is lesson 1.1: Algorithms.
        -   [`115codefilesCSP`][115codefiles] is a set of 3 python turtle programs which move a robot around a maze.
        -   [`csp/art/turtles/project.py`][turtle project] is the lesson project.
    -   [`functions`][funcs] is lesson 1.2: Abstraction.
        -   [`catch-a-turtle`][catch-a-turtle] is a game with a persistant-state leaderboard.

-   ### [`web`](/csp/) is unit 2

    -   `web/project.py` is the unit project.

-   ### `data` is unit 3

    -   `data/project.py` is the unit project.

-   ### `future` is unit 4

    -   `future/project.py` is the unit project.

-   ### Other projects at the [root](./csp/) are listed below

    -   [`bottom_line.py`][bottom line] was made for health. It's a simple python-powered CLI that determines if you have drunk enough water.
    -   [`complaint.py`][complaint] was made for fun in [CSP][art]. It's a python program which makes a `TurtleScreen()` that displays a custom message.

## Tests

To run tests, run `pytest`.

## Use as a template

This repository has been marked as a template. For more information, and instructions for setup, see the [wiki][wiki].
Oh, and please don't cheat. Mrs. Carson is (probably) fine if you use it to check your answers, but don't just copy this. She'll know.

[115codefiles]: /csp/art/turtles/115codefilesCSP/
[ap]: https://apstudents.collegeboard.org/
[art]: #art-is-unit-1-creative-computing-for-all
[black]: https://github.com/psf/black
[bottom line]: /csp/bottom_line.py
[catch-a-turtle]: /csp/art/functions/catch_a_turtle
[csp]: https://apstudents.collegeboard.org/courses/ap-computer-science-principles
[complaint]: /csp/compaint.py
[funcs]: /csp/art/functions/
[pltw]: https://www.pltw.org/
[pltw csp]: https://www.pltw.org/our-programs/pltw-computer-science
[pylint]: https://github.com/PyCQA/pylint
[pytest]: https://pytest.org/
[turtles folder]: /csp/art/turtles/
[turtle project]: /csp/art/turtles/project.py
[wiki]: https://github.com/lishaduck/CSP/wiki
