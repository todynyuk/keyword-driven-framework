import pytest
from src.rozetka_methods.Rozetke_Shopping_Basket_Interpreter import buy_method
from unittest import TestCase


class DriverTestCase(TestCase):

    @pytest.mark.maintainer("todynyuk")
    def testUsualPriceItemAndInBasket(self):
        buy_method()

    @pytest.mark.maintainer("todynyuk")
    def testAddGoodsInBasketAndCheckItEmpty(self):
        buy_method()
