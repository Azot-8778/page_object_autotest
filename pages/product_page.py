import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_message_product_name()
        self.should_be_message_about_cost()
        self.should_be_message_about_basket_total()
        self.should_be_message_about_adding()

        self.message_and_product_name_should_be_equal()
        self.basket_and_product_price_should_be_equal()


    def should_be_message_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not presented"

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Message about adding is not presented"

    def message_and_product_name_should_be_equal(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        #print(f'message: {message}, product name: {product_name}')
        assert product_name == message, \
            "No product name in the message"

    def should_be_message_about_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            "Product cost is not presented"

    def should_be_message_about_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), \
            "Basket total sum is not presented"

    def basket_and_product_price_should_be_equal(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        #print(f'product cost: {product_cost}, basket total: {basket_total}')
        assert product_cost == basket_total, \
            "Product cost not equal to basket in basket"


