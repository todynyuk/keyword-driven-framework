from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import re, time


def openApplication(driver, url):
    driver.get(url)


def enterInTextField(driver, loc, locValue, testdata):
    if (loc == "id"):
        driver.find_element(By.XPATH, locValue).clear()
        driver.find_element(By.ID, locValue).send_keys(testdata)
    if (loc == "css"):
        driver.find_element(By.XPATH, locValue).clear()
        driver.find_element(By.CSS_SELECTOR, locValue).send_keys(testdata)
    if (loc == "name"):
        driver.find_element(By.XPATH, locValue).clear()
        driver.find_element(By.CLASS_NAME, locValue).send_keys(testdata)
    if (loc == "xpath"):
        driver.execute_script("window.scrollTo(0, 300)")
        driver.find_element(By.XPATH, locValue).clear()
        driver.find_element(By.XPATH, locValue).send_keys(int(testdata))


def get_goods_title_text(driver, xpath):
    buffer = driver.find_elements(By.XPATH, xpath)
    goods_title_texts = []
    for elem in buffer:
        goods_title_texts.append(str(elem.text).lower())
    return goods_title_texts


def check_is_all_goods_available(driver, xpath):
    status_text_list = []
    driver.execute_script("window.scrollTo(0, 220)")
    is_available_status_text_list = driver.find_elements(By.XPATH, xpath)
    for elem in is_available_status_text_list:
        status_text_list.append(elem.text)
    time.sleep(3)
    return status_text_list.__len__()


def get_prices_list(driver, xpath):
    choosen_price_devices = []
    for elem in driver.find_elements(By.XPATH, xpath):
        choosen_price_devices.append(re.sub('\D', '', elem.text))
    return choosen_price_devices


def check_is_all_goods_prices_less_than_choosen(driver, xpath, chosen_max_price):
    return all(int(i) <= int(chosen_max_price) for i in get_prices_list(driver, xpath))


def verify_is_search_think_present_in_goods_title(driver, xpath, think_name):
    goods_title_texts = [x.lower() for x in get_goods_title_text(driver, xpath)]
    res = all([ele for ele in str(think_name).lower() if (ele in goods_title_texts)])
    return res


def click(driver, category_parameter, loc, locValue):
    if (loc == "id"):
        driver.find_element(By.ID, locValue).click()
    if (loc == "css"):
        driver.find_element(By.CSS_SELECTOR, locValue).click()
    if (loc == "name"):
        driver.find_element(By.CLASS_NAME, locValue).click()
    if (loc == "xpath"):
        if (locValue == category_parameter):
            driver.find_element(By.XPATH, locValue).click()
        else:
            driver.execute_script("window.scrollTo(0, 300)")
            driver.find_element(By.XPATH, locValue).click()


def move_to(driver, direction):
    if (direction == "top"):
        driver.execute_script("window.scrollTo(0, 220)")
    if (direction == "bottom"):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if (direction == "center"):
        driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'})")


def getElementText(driver, loc, locValue):
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


def check_is_element_present(driver, loc, locValue):
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


def check_is_element_not_present(driver, xpath):
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, xpath)
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
        return False
    return True


def get_elements_count(driver, xpath):
    return int(driver.find_elements(By.XPATH, xpath).__len__())


def check_chosen_filters_contains_chosen_brands(driver, chosen_brand):
    chosen_filters = []
    chosen_filtersText = driver.find_elements(By.XPATH,
                                              "//li[contains(@class,'selection')]//a[contains(@class,'link')]")
    for i in chosen_filtersText:
        chosen_filters.append(str(i.text).replace(' ', ''))
    return chosen_filters.__contains__(chosen_brand)


def isAddedToCartGoodsCounterTextPresent(driver, cart_counter_xpath):
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, cart_counter_xpath)
    except NoSuchElementException:
        return False
    return True


def clickDropdownOption(driver, xpath):
    driver.implicitly_wait(3)
    option = driver.find_element(By.XPATH, xpath)
    option.click()
    time.sleep(3)


def isAllGoodsSortedFromLowToHighPrice(driver, xpath):
    counter_low_hight = 0
    priceItemText = driver.find_elements(By.XPATH, xpath)
    for x in range(1, 6):
        if (re.sub(r'\D', '', priceItemText[x].text)) <= (re.sub(r'\D', '', priceItemText[x + 1].text)):
            counter_low_hight += 1
        else:
            counter_low_hight += 0
    return counter_low_hight


def isAllGoodsSortedFromHighToLowPrice(driver, xpath):
    counter_hight_to_low = 0
    priceItemText = driver.find_elements(By.XPATH, xpath)
    for x in range(1, 6):
        if (re.sub(r'\D', '', priceItemText[x].text)) >= (re.sub(r'\D', '', priceItemText[x + 1].text)):
            counter_hight_to_low += 1
        else:
            counter_hight_to_low += 0
    return counter_hight_to_low


def closeApplication(driver):
    driver.close()
    driver.quit()
