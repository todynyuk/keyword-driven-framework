import time
from src.conftest import setup
from src.rozetka_methods.Keyword_Methods import openApplication, enterInTextField, click, \
    closeApplication, getElementText,check_is_element_present

def search_method():
    sheet, rowCount, driver = setup()
    expected_search_text = sheet.cell_value(3, 4)
    good_title_text = ""
    for i in range(1, rowCount):
        keyword = sheet.cell_value(i, 3)
        if (keyword == "enter url"):
            openApplication(sheet.cell_value(2, 4))

        if (keyword == "send keys"):
            enterInTextField(sheet.cell_value(3, 1), sheet.cell_value(3, 2), sheet.cell_value(3, 4))

        if (keyword == "click"):
            time.sleep(3)
            click(sheet.cell_value(4, 1), sheet.cell_value(4, 2))

        if (keyword == "get search text"):
            time.sleep(3)
            good_title_text = getElementText(sheet.cell_value(i, 1), sheet.cell_value(i, 2))

        if (keyword == "check not found text"):
            check_is_element_present(sheet.cell_value(5, 1),sheet.cell_value(5, 2))

        if (keyword == "verify search text"):
            assert str(good_title_text).lower().__contains__(str(expected_search_text).lower())
            print("\n")
            print("This fifth step is working")

        if (keyword == "quit"):
            closeApplication()
