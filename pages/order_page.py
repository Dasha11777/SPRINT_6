from pages.base_page import BasePage
from locators.locators_landing_page import Testlocators
from locators.locators_order_page import Order_page_locators
import allure
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем форму оформления заказа кликом по "Заказать" в шапке лэндинга')
    def click_on_element_make_order_header(self, button: object) -> object:
        if button == 'header_button':
            self.click_on_element(Testlocators.Button_make_order_header)
        elif button == 'page_button':
            self.scroll_to_element(Testlocators.Button_make_order_landing)
            self.click_on_element(Testlocators.Button_make_order_landing)

    @allure.step('Убедиться, что страница заказа загрузилась (проверяем видимость поля Имя)')
    def name_field_find_element_with_wait(self):
        self.find_element_with_wait(Order_page_locators.INPUT_NAME).is_enabled()

    @allure.step('Заполняем поля "Имя"')
    def fill_name_field(self, name):
        self.find_element_with_wait(Order_page_locators.INPUT_NAME).send_keys(name)

    @allure.step('Заполняем поля "Фамилия"')
    def fill_surname_field(self, surname):
        self.find_element_with_wait(Order_page_locators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполняем поля "Адрес"')
    def fill_adress_field(self, adress):
        self.find_element_with_wait(Order_page_locators.INPUT_ADRESS).send_keys(adress)

    @allure.step('В форме создания заказа выбираем станцию метро')
    def select_metro(self, station):
        self.click_on_element(Order_page_locators.INPUT_METRO)
        self.find_element_with_wait(Order_page_locators.INPUT_METRO).send_keys(station)
        self.find_element_with_wait(Order_page_locators.INPUT_METRO).send_keys(Keys.DOWN, Keys.ENTER)

    @allure.step('Заполняем поле Телефон')
    def fill_phone_field(self, phone):
        self.find_element_with_wait(Order_page_locators.INPUT_PHONE_NUMBER).send_keys(phone)

    @allure.step('Кликом по Далее переходим на вторую страницу формы заказа')
    def click_on_element_next(self):
        self.click_on_element(Order_page_locators.BUTTON_NEXT)

    @allure.step('Выбираем дату заказа')
    def pick_date(self, date):
        self.find_element_with_wait(Order_page_locators.INPUT_DATE).send_keys(date)
        self.find_element_with_wait(Order_page_locators.INPUT_DATE).send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды')
    def pick_rental_period(self, period):
        self.click_on_element(Order_page_locators.RENTAL_PERIOD)        
        rental_period_locator = Order_page_locators.get_rental_period_locator(period)
        self.find_element_with_wait(rental_period_locator)
        self.click_on_element(rental_period_locator)

    @allure.step('Выбираем цвет самоката')
    def pick_color(self, color):
        color_locator = Order_page_locators.get_color_locator(color)
        self.click_on_element(color_locator)

    @allure.step('Заполняем поле Комментарий')
    def fill_comment_field(self, comment):
        self.find_element_with_wait(Order_page_locators.INPUT_COMMENT).send_keys(comment)

    @allure.step('Клик по кнопке Заказать в конце формы заказа')
    def click_on_element_create_order(self):
        self.click_on_element(Order_page_locators.CREATE_ORDER)

    @allure.step('Клик по кнопке Да - подтверждение заказа')
    def click_on_element_confirm_order_yes(self):
       self.click_on_element(Order_page_locators.BUTTON_CONFIRM_ORDER_YES)
        
    @allure.step('Проверяем, что заказ оформлен успешно')
    def is_order_successful(self) -> bool:
        try:
            el = self.wait_order_success_visible(timeout=15)
            return el.is_displayed()
        except Exception:
            return False





