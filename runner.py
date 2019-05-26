from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from helpers import get_info_by_elements
from pages import StartPage, RECOMMENDED, RECOMMENDED, DATE, NAME, PRICE_MIN, PRICE_MAX, BRAND


def app(min_price, max_price, sorting_type, search_string):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    browser = WebDriver(chrome_options=chrome_options)
    browser.get("https://iledebeaute.ru/")
    start = StartPage(browser)
    products_page = start.search_by_name(search_string)
    products_page.pick_sorting(sorting_type)
    products_page.pick_price(min_price, max_price)
    products_list = products_page.get_all_products()
    print(get_info_by_elements(products_list))
    browser.quit()
