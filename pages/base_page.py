from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from urls import Urls
import allure

class BasePage:
    BASE_URL = Urls.BASE_URL

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открываем главную страницу")
    def open_url(self):
        self.driver.get(self.BASE_URL)

    @allure.step("Прокручиваем страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Прокручиваем до элемента с ожиданием")
    def scroll_into_view(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Ищем элемент с ожиданием")
    def find_element_with_wait(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Кликаем на элемент")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        # Дожидаемся, что элемент станет кликабельным
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        
        try:
            element.click()
        except ElementClickInterceptedException:
            # Если обычный клик не сработал из-за перекрытия элемента, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получаем текст из элемента")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получаем все дескрипторы окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключаемся на окно по индексу")
    def switch_to_window_by_index(self, index):
        handles = self.get_window_handles()
        if index < len(handles):
            self.driver.switch_to.window(handles[index])
        else:
            raise IndexError(f"Window index {index} is out of range. Available windows: {len(handles)}")

    @allure.step("Получаем количество открытых окон")
    def get_windows_count(self):
        return len(self.get_window_handles())