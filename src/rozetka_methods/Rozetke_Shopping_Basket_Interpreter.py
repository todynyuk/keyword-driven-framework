import time
import re
from src.conftest import setup
from src.rozetka_methods.Keyword_Methods import openApplication, click, closeApplication, getElementText, \
    enterInTextField, check_is_element_not_present, get_elements_count


def buy_method():
    sheet, rowCount, driver = setup()
    elements_text_list = []
    elements_count = 0
    for i in range(1, rowCount):
        keyword = sheet.cell_value(i, 3)
        if (keyword == "enter url"):
            openApplication(driver, sheet.cell_value(2, 4))

        if (keyword == "click"):
            if (sheet.cell_value(i, 2) != ""):
                time.sleep(3)
                click(driver, sheet.cell_value(3, 2), sheet.cell_value(i, 1), sheet.cell_value(i, 2))

        if (keyword == "get element text"):
            time.sleep(3)
            element_text = getElementText(driver, sheet.cell_value(i, 1), sheet.cell_value(i, 2))
            elements_text_list.append(element_text)

        if (keyword == "send keys"):
            enterInTextField(sheet.cell_value(i, 1), sheet.cell_value(13, 2), sheet.cell_value(13, 4))

        if (keyword == "check is element not present"):
            assert (check_is_element_not_present(driver, sheet.cell_value(7, 2))) == False, "Element is presented"

        if (keyword == "get elements count"):
            elements_count = get_elements_count(driver, sheet.cell_value(8, 2))

        if (keyword == "verify parameters"):
            assert str(elements_text_list[1]).lower().__contains__(str(elements_text_list[2]).lower())

        if (keyword == "verify elements count"):
            assert elements_count > 0, "Elements count == 0"

        if (keyword == "compare values"):
            assert int(re.sub(r'\D', '', elements_text_list[0])) == int(re.sub(r'\D', '', elements_text_list[3]))
            if (elements_text_list.__len__() > 4):
                print("Actual: ", (int(re.sub(r'\D', '', elements_text_list[3]))) * (int(sheet.cell_value(13, 4))))
                print("Expected: ", int(re.sub(r'\D', '', elements_text_list[4])))
                assert (int(re.sub(r'\D', '', elements_text_list[3]))) * (int(sheet.cell_value(13, 4))) == int(
                    re.sub(r'\D', '', elements_text_list[4]))

        if (keyword == "quit"):
            closeApplication(driver)
