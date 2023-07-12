import os

from selenium import webdriver
import xlrd

def setup():
    global sheet
    global rowCount
    base_path = os.path.dirname(os.path.realpath(__file__))
    workbook = xlrd.open_workbook(
        f"{base_path}/tests/resources/web_sheet.xls")
    # sheet = workbook.sheet_by_name("Sheet7")
    # sheet = workbook.sheet_by_name("Sheet8")
    # sheet = workbook.sheet_by_name("Sheet9")
    # sheet = workbook.sheet_by_name("Sheet10")
    sheet = workbook.sheet_by_name("Sheet11")
    rowCount = sheet.nrows
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return sheet, rowCount, driver
