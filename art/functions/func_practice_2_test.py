"""Tests the func_practice_2.py module.
"""
import unittest
import func_practice_2
import pytest

# content of test_sample.py


class TripleTest(unittest.TestCase):
    """This class contains tests.

    It is used to remind me how tests are made.
    """

    @pytest.mark.task(taskno=1)
    def test_for_four(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.triple(4), 12)

    @pytest.mark.task(taskno=2)
    def test_for_five(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.triple(5), 15)


class AreaTest(unittest.TestCase):
    """This class contains tests.

    It is used to remind me how tests are made.
    """

    @pytest.mark.task(taskno=1)
    def test_for_four(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.triangle_area(1, 1), 0.5)

    @pytest.mark.task(taskno=2)
    def test_for_five(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.triangle_area(5, 4), 10)


class MinTest(unittest.TestCase):
    """This class contains tests.

    It is used to remind me how tests are made.
    """

    @pytest.mark.task(taskno=1)
    def test_for_one(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.min_val(1, 1), 1)

    @pytest.mark.task(taskno=2)
    def test_for_four(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.min_val(5, 4), 4)

    @pytest.mark.task(taskno=3)
    def test_for_five(self):
        """Tests that triple works."""
        self.assertEqual(func_practice_2.min_val(10, 14), 10)
