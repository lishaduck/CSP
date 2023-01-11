"""Tests ap_2023."""


from src.ap_2023 import main
import tkinter as tk

import pytest

# TODO: add actual test
class TestMain:
    """This class contains tests."""

    @pytest.fixture()
    def make_window(self):
        root = main.App()
        yield root

    @pytest.fixture()
    def define_tk(self):
        return tk.Tk

    def test_default(self, make_window, define_tk):
        """Tests that the --default CLI option works."""
        assert isinstance(make_window, define_tk)
