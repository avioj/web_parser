from selenium.webdriver.common.by import By

SEARCH_SELECTOR = By.XPATH, "//input[@placeholder='Поиск']"
SORT_BY_DROP_DOWN = By.ID, "showcaseFilterSort"
MIN_PRICE_INPUT = By.XPATH, "//input[@class='price__min']"
MAX_PRICE_INPUT = By.XPATH, "//input[@class='price__max']"
APPLY_BUTTON = By.XPATH, "//a[@class='apply arrow-left-container']"
PARENT_OF_PRODUCTS = By.XPATH, "//div[@class='_js-mobile-showcase-container b-mobile-showcase cf']"
PRICE_BY_PRODUCT_SELECTOR = By.XPATH, ".//*[contains(@class, 'price')]"
BRAND_BY_PRODUCT_SELECTOR = By.XPATH, ".//*[contains(@class, 'brand')]"
PICK_SORTING_PATTERN = ".//option[@value='{}']"
