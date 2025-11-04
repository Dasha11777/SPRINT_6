from selenium.webdriver.common.by import By

class Order_page_locators:

    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]')
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = [By.CSS_SELECTOR, 'div[class="Dropdown-root"]']
    
    @staticmethod
    def get_rental_period_locator(period):
        """Возвращает локатор для выбора срока аренды с переданным периодом"""
        return (By.XPATH, f'//div[text()="{period}"]')
    
    @staticmethod
    def get_color_locator(color):
        """Возвращает локатор для выбора цвета самоката"""
        return (By.XPATH, f'//input[@id="{color}"]')

    INPUT_COMMENT = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='Комментарий для курьера']")
    CREATE_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    BUTTON_CONFIRM_ORDER_YES = [By.XPATH, '//button[text()="Да"]']

    ORDER_SUCCESS_MESSAGE = (By.XPATH, '//div[contains(text(),"Заказ оформлен")]')
