import allure


@allure.epic("Сайт demoqa.com")
@allure.feature("Навигация по разделам")
class TestDemoqaNavigation:

    @allure.title('Проверка перехода на страницу раздела "Elements"')
    def test_go_to_elements_section(self, demoqa_for_python_main):

        with allure.step("Откроем главную страницу https://demoqa.com"):
            demoqa_for_python_main.open()


        with allure.step('Нажмём на карточку "Elements"'):
            demoqa_for_python_main.go_to_elements()

        with allure.step(
            "Проверим, что пункт меню 'Text Box' отображается в сайдбаре"
        ):
            demoqa_for_python_main.elements_sidebar_items.item(0).check_visible()



    @allure.title('Проверка перехода на страницу раздела "Book Store Application"')
    def test_go_to_book_store_section(self, demoqa_for_python_main):
        with allure.step("Откроем главную страницу https://demoqa.com"):
            demoqa_for_python_main.open()

        with allure.step('Нажмём на карточку "Book Store Application"'):
            demoqa_for_python_main.go_to_book_store()

        with allure.step(
            'Проверим наличие таблицы книг и кнопки "Login" на странице '
            '"Book Store Application"'
        ):
            demoqa_for_python_main.book_store_table_rows.item(0).check_visible()
            demoqa_for_python_main.book_store_login_button.check_visible()
