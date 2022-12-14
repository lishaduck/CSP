"""Tests the func_practice_2.py module."""


from src.csp.art.functions import func_practice_2


class TripleTest:
    """This class contains tests for the triple function."""

    def test_for_four(self):
        """Tests that triple works with 4 --> 12."""
        assert func_practice_2.triple(4) == 12

    def test_for_five(self):
        """Tests that triple works with 5 --> 15."""
        assert func_practice_2.triple(5) == 15


class AreaTest:
    """This class contains tests for the triangle_area function."""

    def test_for_four(self):
        """Tests that area works given 1 and 1."""
        assert func_practice_2.triangle_area(1, 1) == 0.5

    def test_for_five(self):
        """Tests that area works given 5 and 4."""
        assert func_practice_2.triangle_area(5, 4) == 10


class MinTest:
    """This class contains tests for the min_test."""

    def test_for_one(self):
        """Tests that min_val works given two equal values."""
        assert func_practice_2.min_val(1, 1) == 1

    def test_for_four(self):
        """Tests that min_val works given 5 and 4."""
        assert func_practice_2.min_val(5, 4) == 4

    def test_for_five(self):
        """Tests that triple works."""
        assert func_practice_2.min_val(10, 14) == 10
