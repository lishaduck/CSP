"""Tests the average.py module.
"""


import random
import statistics
import unittest

import average
import pytest


class AverageTest(unittest.TestCase):
    """This class contains tests.

    It is used to remind me how tests are made.
    """

    @pytest.mark.task(taskno=1)
    def test_default(self):
        """Tests that the --default CLI option works."""
        self.assertEqual(average.average(average.scores), 8.5)

    @pytest.mark.task(taskno=2)
    def test_fuzz(self):
        """Tests that with random numbers, that function performs on par with `statistics.mean`."""
        fuzz = [
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
            random.randint(-50, 50),
        ]
        self.assertEqual(statistics.mean(fuzz), average.average(fuzz))
