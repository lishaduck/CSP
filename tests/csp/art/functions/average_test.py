"""Tests the average.py module."""


import random
import statistics

from src.csp.art.functions import average


class AverageTest:
    """This class contains tests.

    It is used to remind me how tests are made.
    """

    def test_default(self):
        """Tests that the --default CLI option works."""
        assert average.average(average.scores) == 8.5

    def test_fuzz(self):
        """Tests that the function performs on par with `statistics.mean`.

        Fuzzes with `random` numbers, not `hypothesis`.
        """
        fuzz = [
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
        ]
        assert statistics.mean(fuzz) == average.average(fuzz)
