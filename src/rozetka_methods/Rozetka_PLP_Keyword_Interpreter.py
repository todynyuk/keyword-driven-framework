import time
from src.conftest import setup
from src.rozetka_methods.Keyword_Methods import openApplication, click, closeApplication, getElementText, \
    check_chosen_filters_contains_chosen_brands, clickDropdownOption, isAllGoodsSortedFromLowToHighPrice, \
    isAllGoodsSortedFromHighToLowPrice, enterInTextField, check_is_all_goods_prices_less_than_choosen, \
    verify_is_search_think_present_in_goods_title, check_is_all_goods_available, isAddedToCartGoodsCounterTextPresent


def filter_method():
    sheet, rowCount, driver = setup()
    brands_text_list = []
    for i in range(1, rowCount):
        keyword = sheet.cell_value(i, 3)
        if (keyword == "enter url"):
            openApplication(driver, sheet.cell_value(2, 4))

        if (keyword == "click"):
            if (sheet.cell_value(i, 2) != ""):
                time.sleep(3)
                click(driver, sheet.cell_value(3, 2), sheet.cell_value(i, 1), sheet.cell_value(i, 2))

        if (keyword == "sendkeys"):
            enterInTextField(driver, sheet.cell_value(7, 1), sheet.cell_value(7, 2), sheet.cell_value(7, 4))

        if (keyword == "vefify filter max price"):
            check_is_all_goods_prices_less_than_choosen(driver, sheet.cell_value(9, 2), sheet.cell_value(7, 4))

        if (keyword == "select from dropdown"):
            if (str(sheet.cell_value(i, 2)).startswith("//option")):
                clickDropdownOption(driver, sheet.cell_value(i, 2))
            elif (str(sheet.cell_value(i, 2)).startswith("//select")):
                clickDropdownOption(driver, sheet.cell_value(i, 2))

        if (keyword == "verify sorting from low to high"):
            assert isAllGoodsSortedFromLowToHighPrice(driver,
                                                      sheet.cell_value(6,
                                                                       2)) == 5, "One or more prices not sorted from low to high price"
            print("sort from low to high pass")

        if (keyword == "verify sorting from high to low"):
            assert isAllGoodsSortedFromHighToLowPrice(driver,
                                                      sheet.cell_value(8,
                                                                       2)) == 5, "One or more prices not sorted from high to low price"

        if (keyword == "get element text"):
            time.sleep(3)
            element_text = getElementText(driver, sheet.cell_value(i, 1), sheet.cell_value(i, 2))
            brands_text_list.append(element_text)

        if (keyword == "verify if brand choosen"):
            brands_text_list.append(sheet.cell_value(5, 4))
            brands_text_list.append(sheet.cell_value(6, 4))
            brands_text_list.append(sheet.cell_value(7, 4))
            for k in range(1, brands_text_list.__len__() - 1):
                check_chosen_filters_contains_chosen_brands(driver, brands_text_list[k])

        if (keyword == "check isn't cart counter  present"):
            assert isAddedToCartGoodsCounterTextPresent(driver, sheet.cell_value(5, 2)) == False, \
                "Cart Goods Counter Text is presented"

        if (keyword == "check is cart counter  present"):
            assert isAddedToCartGoodsCounterTextPresent(driver, sheet.cell_value(7, 2)) != False, \
                "Cart Goods Counter Text isn't presented"

        if (keyword == "verify is goods title contains brand"):
            verify_is_search_think_present_in_goods_title(driver, sheet.cell_value(10, 2), sheet.cell_value(10, 4))

        if (keyword == "vefify all goods are available"):
            assert check_is_all_goods_available(driver,
                                                sheet.cell_value(12, 2)) == 0, "One or more goods are not available"

        if (keyword == "quit"):
            closeApplication(driver)
