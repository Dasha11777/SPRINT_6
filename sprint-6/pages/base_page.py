from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/' # URL здесь

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self):
        self.driver.get(self.BASE_URL)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_into_view(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def find_element_with_wait(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        # Дожидаемся, что элемент станет кликабельным
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        
        try:
            element.click()
        except ElementClickInterceptedException:
            # Если обычный клик не сработал из-за перекрытия элемента, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    def get_current_url(self):
        return self.driver.current_url