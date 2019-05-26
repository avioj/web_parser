from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from helpers import get_info_by_elements
from pages import StartPage, RECOMMENDED

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-maximized")
browser = WebDriver(chrome_options=chrome_options)
browser.get("https://iledebeaute.ru/")
start = StartPage(browser)
products_page = start.search_by_name("esc")
products_page.pick_sorting(RECOMMENDED)
products_page.pick_price(123, 8000)
products_list = products_page.get_all_products()
print(get_info_by_elements(products_list))
browser.quit()