import time
import re
from src.conftest import setup
from src.rozetka_methods.Keyword_Methods import openApplication, click, closeApplication, getElementText, move_to


def filter_method():
    sheet, rowCount, driver = setup()
    ram_value = str(sheet.cell_value(5, 4))
    elements_text_list = []
    for i in range(1, rowCount):
        keyword = sheet.cell_value(i, 3)
        if (keyword == "enter url"):
            openApplication(driver, sheet.cell_value(2, 4))

        if (keyword == "move to"):
            move_to(driver, sheet.cell_value(7, 4))

        if (keyword == "click"):
            if (driver, sheet.cell_value(3, 2), sheet.cell_value(i, 2) != ""):
                time.sleep(3)
                click(driver, sheet.cell_value(3, 2), sheet.cell_value(i, 1), sheet.cell_value(i, 2))

        if (keyword == "get element text"):
            time.sleep(3)
            element_text = getElementText(driver, sheet.cell_value(i, 1), sheet.cell_value(i, 2))
            elements_text_list.append(element_text)

        if (keyword == "verify parameters"):
            assert str(element_text).lower().__contains__(str(ram_value).lower())

        if (keyword == "compare values"):
            assert int(re.sub(r'\D', '', elements_text_list[0])) == int(re.sub(r'\D', '', elements_text_list[2]))

        if (keyword == "quit"):
            closeApplication(driver)
