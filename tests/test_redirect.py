from pages.landing_page import LandingPage
from pages.redirect_page import RedirectPage
from urls import Urls
import allure

class TestRedirectPage:

    @allure.title("Проверка редиректа на главную страницу Я.Самокат")
    def test_logo_redirect(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_url()

        with allure.step(f"Проверяем переход на главную страницу Я.Самокат при клике на Лого сервиса в шапке"):
            landing_page.click_on_order_button()

            logo_page = RedirectPage(driver)
            logo_page.click_on_logo_scooter()
            assert logo_page.get_current_url() == Urls.BASE_URL

    @allure.title("Проверка редиректа на главную страницу Яндекс.Дзен")
    def test_logo_redirect_dzen(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_url()

        with allure.step('Проверяем редирект при клике на логотип яндекса в хедере.'):
            redirect_dzen_test = RedirectPage(driver)
            redirect_dzen_test.click_on_logo_yandex()

            # Переключаемся на новую вкладку:
            assert redirect_dzen_test.get_windows_count() == 2
            redirect_dzen_test.switch_to_window_by_index(1)
            redirect_dzen_test.find_element_find_button()
            final_url = redirect_dzen_test.get_current_url()
            assert Urls.YANDEX_DZEN_DOMAIN in final_url