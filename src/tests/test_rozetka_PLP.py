import pytest
from src.rozetka_methods.Rozetka_PLP_Keyword_Interpreter import filter_method
from unittest import TestCase


class DriverTestCase(TestCase):

    @pytest.mark.maintainer("todynyuk")
    def testVerifySortByPrice(self):
        filter_method()

    @pytest.mark.maintainer("todynyuk")
    def testChooseBrandsAndCheck(self):
        filter_method()

    @pytest.mark.maintainer("todynyuk")
    def testFilterByBrandNameMaxCustomPriceAndAvailable(self):
        filter_method()

    @pytest.mark.maintainer("todynyuk")
    def testAddingAndCountGoodsInBasket(self):
        filter_method()
