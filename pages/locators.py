from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    EMAIL_REGISTER = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTER = (By.CSS_SELECTOR, '##id_registration-password1')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    REGISTER_FORM = (By.ID, "register_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price_color")

class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner h2")


