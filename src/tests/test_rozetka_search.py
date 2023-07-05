import pytest
from src.rozetka_methods.Rozetka_Search_Page_Keyword_Interpreter import search_method
from unittest import TestCase


class DriverTestCase(TestCase):

    @pytest.mark.label("Search", "correct")
    def test_correct_search(self):
        search_method()

    @pytest.mark.label("Search", "incorrect")
    def test_incorrect_search(self):
        search_method()
