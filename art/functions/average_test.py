"""Tests the average.py module.
"""
import random
import statistics
import average

# content of test_sample.py


class TestClass:
    """This class contains tests.

    It is used to remind me how tests are made.
    """

    def test_default(self):
        """Tests that the --default CLI option works."""
        assert average.average(average.scores) == 8.5

    def test_fuzz(self):
        fuzz = [
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
        ]
        assert statistics.mean(fuzz) == average.average(fuzz)
