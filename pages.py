
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import SEARCH_SELECTOR, SORT_BY_DROP_DOWN, MIN_PRICE_INPUT, MAX_PRICE_INPUT, APPLY_BUTTON, \
    PARENT_OF_PRODUCTS, PICK_SORTING_PATTERN

# PRODUCT SORTING TYPES
RECOMMENDED, DATE, NAME, PRICE_MIN, PRICE_MAX, BRAND = (
    "recommended", "date", "name", "price_min", "price_max", "brand")


class StartPage:
    def __init__(self, webdriver: WebDriver):
        self.browser = webdriver

    @property
    def search_label(self):
        return self.browser.find_element(*SEARCH_SELECTOR)

    def search_by_name(self, product_name):
        self.search_label.send_keys(product_name)
        self.search_label.send_keys(Keys.ENTER)
        return ProductsPage(self.browser)


class ProductsPage:
    def __init__(self, webdriver: WebDriver):
        self.browser = webdriver

    @property
    def sorting_select(self):
        return self.browser.find_element(*SORT_BY_DROP_DOWN)

    @property
    def min_price_input(self):
        return self.browser.find_element(*MIN_PRICE_INPUT)

    @property
    def max_price_input(self):
        return self.browser.find_element(*MAX_PRICE_INPUT)

    @property
    def apply_price(self):
        return self.browser.find_element(*APPLY_BUTTON)

    @property
    def products_parent(self):
        return self.browser.find_element(*PARENT_OF_PRODUCTS)

    def pick_sorting(self, sorting):
        self.sorting_select.click()
        self.sorting_select.find_element(By.XPATH, PICK_SORTING_PATTERN.format(sorting)).click()

    def pick_price(self, minimal, maximal):
        self.min_price_input.click()
        self.min_price_input.clear()
        self.min_price_input.send_keys(minimal)

        self.max_price_input.click()
        self.max_price_input.clear()
        self.max_price_input.send_keys(maximal)
        self.max_price_input.send_keys(Keys.ENTER)
        # ActionChains(self.browser).click(self.apply_price).perform()
        self.apply_price.click()

    def get_all_products(self):
        return self.products_parent.find_elements_by_xpath(".//div")

