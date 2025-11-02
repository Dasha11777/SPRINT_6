
from pages.landing_page import LandingPage
from data import LandingAnswers
import allure
import pytest

@pytest.mark.parametrize("question_num, expected_answer", LandingAnswers.ANSWERS.items())
def test_landing_page(driver, question_num, expected_answer):
    allure.dynamic.title(f"Проверка FAQ: вопрос №{question_num}")

    landing_page = LandingPage(driver)
    landing_page.open_url()
    landing_page.scroll_to_questions()

    with allure.step(f"Проверяем вопрос №{question_num}"):
        landing_page.click_on_question(question_num)

        # Дожидаемся появления текста ответа (лучше реализовать в методе страницы)
        answer_text = landing_page.get_answer_text(question_num).strip()

        assert answer_text == expected_answer.strip(), (
            f"Ответ для вопроса №{question_num} не совпадает с ожидаемым.\n"
            f"Ожидалось: {expected_answer}\nПолучено: {answer_text}"
        )
