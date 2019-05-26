from constants import PRICE_BY_PRODUCT_SELECTOR, BRAND_BY_PRODUCT_SELECTOR


def get_info_by_element(element):
    price = element.find_element(*PRICE_BY_PRODUCT_SELECTOR).text
    brand = element.find_element(*BRAND_BY_PRODUCT_SELECTOR).text
    title = element.text
    return price, brand, title


def get_info_by_elements(elements):
    return [get_info_by_element(element) for element in elements]
