from selenium.webdriver.common.by import By

from src.conftest import setup

global sheet, rowCount, driver
sheet, rowCount, driver = setup()


def openApplication(url):
    driver.get(url)


def enterInTextField(loc, locValue, testdata):
    if (loc == "id"):
        driver.find_element(By.ID, locValue).send_keys(testdata)
    if (loc == "css"):
        driver.find_element(By.CSS_SELECTOR, locValue).send_keys(testdata)
    if (loc == "name"):
        driver.find_element(By.CLASS_NAME, locValue).send_keys(testdata)
    if (loc == "xpath"):
        driver.find_element(By.XPATH, locValue).send_keys(testdata)


def click(loc, locValue):
    if (loc == "id"):
        driver.find_element(By.ID, locValue).click()
    if (loc == "css"):
        driver.find_element(By.CSS_SELECTOR, locValue).click()
    if (loc == "name"):
        driver.find_element(By.CLASS_NAME, locValue).click()
    if (loc == "xpath"):
        driver.find_element(By.XPATH, locValue).click()


def move_to(direction):
    if (direction == "top"):
        driver.execute_script("window.scrollTo(0, 220)")
    if (direction == "bottom"):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if (direction == "center"):
        driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'})")


def getElementText(loc, locValue):
    element_text = ""
    if (loc == "id"):
        element_text = driver.find_element(By.ID, locValue).text
    if (loc == "css"):
        element_text = driver.find_element(By.CSS_SELECTOR, locValue).text
    if (loc == "name"):
        element_text = driver.find_element(By.CLASS_NAME, locValue).text
    if (loc == "xpath"):
        element_text = driver.find_element(By.XPATH, locValue).text
    return element_text


def check_is_element_present(loc, locValue):
    is_element_present = False
    if (loc == "id"):
        is_element_present = driver.find_element(By.ID, locValue).is_displayed()
    if (loc == "css"):
        is_element_present = driver.find_element(By.CSS_SELECTOR, locValue).is_displayed()
    if (loc == "name"):
        is_element_present = driver.find_element(By.CLASS_NAME, locValue).is_displayed()
    if (loc == "xpath"):
        is_element_present = driver.find_element(By.XPATH, locValue).is_displayed()
    return is_element_present


def closeApplication():
    driver.close()
    driver.quit()
