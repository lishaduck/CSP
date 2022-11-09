"""Program: unscramble_game.py - Play a fun game!

"""


import dataclasses
import random


# Create a list of words for the computer to choose from
word_list_1 = [
    ".NET",
    "gitignore",
    "jupyter",
    "markdown",
    "NetLogo",
    "javascript",
    "TypeScript",
    "flow",
    "react",
    "preact",
    "JSON",
    "CSS",
    "scss",
    "less",
    "stylus",
    "sass",
    "styl",
    "TypeScriptReact",
    "HTML",
    "python",
    "swift",
    "YAML",
    "elm",
    "Java",
    "C",
    "C++",
    "C#",
    "objective-C",
    "objective-C++",
    "elixir",
]
EASTER = "malware"
EGG = "npm-birthday"
word_list_2 = [
    "Go",
    "haxe",
    "pug",
    "jade",
    "Lua",
    "PHP",
    "R",
    "REST",
    "GraphQL",
    "CodeQL",
    "ruby",
    "rust",
    "PowerShell",
    "VHDL",
    "Z80",
    EASTER,
    "WebAssembly",
    "clojure",
    "CoffeeScript",
    "dart",
    "diff",
    "Docker",
    "F#",
    "groovy",
    "HandleBars",
    "HLSL",
    "GLSL",
    "ini",
    "julia",
    "LaTeX",
    "log",
    "make",
    "Perl",
    "Razor",
    "reStructuredText",
    "Shaderlab",
    "shell",
    "SQL",
    "VisualBasic",
    "WindowsBat",
    "XML",
    "mermaid",
    "GeoJSON",
    "TopoJSON",
    "ASCII STL",
    "ada",
    "apacheconf",
    "applescript",
    "bash",
    "console",
    "erlang",
    "fortran",
    "haskell",
    "markdownReact",
    "postscript",
    "PureScript",
    "protobuf",
    "scala",
    "scheme",
    "text",
    "vim",
    "ESM",
    "commonjs",
    "sarif",
    "StarLogo",
    "Vue",
    "Angular",
    "Ember",
    "Glimmer",
    "roc",
]
words = word_list_1 + word_list_2


# credit where credit is due: https://stackoverflow.com/a/287944
@dataclasses.dataclass
class BColors:
    """Non-comprehensive list of escape codes.

    From:https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# this function will take a word passed in as a parameter and return the same word scrambled
def scramble(w):  # this defines the function
    """"""
    letters = list(w)  # this makes a list of the letters
    random.shuffle(letters)  # this scrambles the letters
    scramble_word = ""  # this initates a string
    for i in letters:  # this is a for loop
        scramble_word = scramble_word + i  # this makes the scrambled word
    return scramble_word  # this makes the word accessable


low_score = 500
total = 0


def instructions():
    # print a statement for the directions
    print(
        f"""
{BColors.HEADER}{BColors.BOLD}
HOW TO PLAY:
{BColors.ENDC}\n
The game will print the {BColors.UNDERLINE}scrambled{BColors.ENDC} name of a programming language.
Then, you will type in your answer.
If it is correct, you'll be prompted to answer another.
If your not, you'll be prompted to try again.
To skip a question, type ':skip' or ':s'.
To end the round, type ':exit', or ':e'.
To quit, type ':quit' or ':q'.
After 10 successes, you'll be given you score.
{BColors.UNDERLINE}Lower{BColors.ENDC} is better.
\n
        """
    )


def game():
    global low_score
    global total

    score = 0
    j = 0
    answer = ""
    while j < 10 and answer not in (":exit", ":e", ":q", ":quit", EGG):
        # define a variable called secret_word and have it pick a random word from the list
        secret_word = random.choice(words)
        print("\n\n" + scramble(secret_word) + "\n")
        answer = "rbt"  # short for `Roc Build Tool`,
        # (continued:) rbt is pronounced 'ribbit', per https://github.com/roc-lang/rbt/
        # Ask the user for their input to guess the word
        while answer not in (
            secret_word,
            ":exit",
            ":e",
            ":skip",
            ":s",
            ":quit",
            ":q",
            EGG,
        ):
            answer = input("")

            if answer not in (secret_word, ":exit", ":e", ":quit", ":q") and (
                secret_word != EASTER and answer is not EGG
            ):
                score = score + 1
        if answer == EGG:
            score = -1
        j = j + 1
    print("\n\n\n")
    print("Score: ", score)
    total = total + score
    print("Total:", total)
    low_score = min(low_score, score)
    print("Low Score:", low_score)
    while answer == EGG:
        print("Score: ", score)
        total = total + score
        print("Total:", total)
        low_score = min(low_score, score)
        print("Low Score:", low_score)


# Entrypoint
if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        is_playing = True
        instructions()
        while is_playing:
            game()
            still_playing = input("Want to play again? (y/n) ")
            if still_playing not in ("Y", "y"):
                is_playing = False
        print("Bye!")
    else:
        print(__doc__)
        want_to_play = input("Do you want to play? (y/n) ")
        if want_to_play in ("Y", "y"):
            instructions()
            is_playing = True

            while is_playing:
                game()
                still_playing = input("Want to play again? (y/n) ")
                if still_playing not in ("Y", "y"):
                    is_playing = False
            print("Bye!")
