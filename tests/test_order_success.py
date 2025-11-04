from pages.order_page import OrderPage
import allure
import pytest
from data import Person

class TestOrderSuccess:

    @allure.title("Тест успешного оформления заказа самоката")
    @pytest.mark.parametrize('button', ['header_button', 'page_button'])
    def test_order_upp_success(self, driver, button):
        order_page = OrderPage(driver)
        order_page.open_url()

        with allure.step(f"Проверяем возможность сделать заказ самоката через кнопку Заказать вверху лэндинга"):
            order_page.click_on_element_make_order_header(button=button)
            order_page.name_field_find_element_with_wait()
            order_page.fill_name_field(Person.random_name)
            order_page.fill_surname_field(Person.random_surname)        
            order_page.fill_adress_field(Person.random_adress)
            order_page.select_metro(Person.random_station)
            order_page.fill_phone_field(Person.random_phone_number)
            order_page.click_on_element_next()
            order_page.pick_date(Person.random_date)
            order_page.pick_rental_period(Person.random_period)
            order_page.pick_color(Person.random_color)
            order_page.fill_comment_field(Person.random_comment)
            order_page.click_on_element_create_order()
            order_page.click_on_element_confirm_order_yes()

            # Проверяем, что заказ оформлен успешно
            assert order_page.is_order_successful(), "Заказ не был оформлен успешно - сообщение об успехе не отображается"
        



