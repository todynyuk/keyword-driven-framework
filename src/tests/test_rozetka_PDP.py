import pytest
from src.rozetka_methods.Rozetka_PDP_Keyword_Interpreter import filter_method
from unittest import TestCase

class DriverTestCase(TestCase):

    @pytest.mark.maintainer("todynyuk")
    def testItemRamAndPrice(self):
        filter_method()