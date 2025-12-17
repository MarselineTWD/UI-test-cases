from playwright.sync_api import Page

from gpn_qa_utils.ui.page_factory.button import Button
from gpn_qa_utils.ui.page_factory.component_list import ComponentList
from gpn_qa_utils.ui.pages.base import BasePage

# review: Можно сократить до DemoqaMain
class DemoqaForPythonMain(BasePage):
    """Главная страница сайта https://demoqa.com."""

    # review: переопределять методы перед __init__ нарушает порядок Python и может запутать IDE/читателей.
    # Правильный порядок: __init__ → методы
    def open(self):
        """
        Переопределяем стандартный open, чтобы:
        - увеличить таймаут навигации
        - не ждать полного load, а только domcontentloaded
        """
        self.browser.page.goto(
            self.url,
            wait_until="domcontentloaded",  # или "commit"
            timeout=60000,                  # 60 секунд вместо 30
        )
        # review: После метода open нет цепочки вызовов, возвращать self не нужно
        return self

    def __init__(self, page: Page):
        super().__init__(page, url="https://demoqa.com/")

        self.page = page
        # review: зачем такой пробел? Если не установлены линтеры, используйте линтеры IDE
        # в pycharm например комбинация (ctrl+alt+l)


        self.button_elements_card = Button(
            page,
            strategy="locator",
            # review: тут и в селекторах ниже, нужно стараться найти максимально короткий селектор, т.к. при изменении
            # одно из элементов тест/ы будут падать
            selector=".category-cards .card.mt-4.top-card:has-text('Elements')",
            allure_name='Карточка "Elements" на главной странице',
        )

        self.button_book_store_card = Button(
            page,
            strategy="locator",
            selector=".category-cards .card.mt-4.top-card:has-text('Book Store Application')",
            allure_name='Карточка "Book Store Application" на главной странице',
        )

        self.elements_sidebar_items = ComponentList(
            page,
            strategy="locator",
            selector='li.btn.btn-light:has-text("Text Box")',
            allure_name='Пункты меню "Text Box" в сайдбаре Elements',
        )



        self.book_store_login_button = Button(
            page,
            strategy="locator",
            selector="#login",
            allure_name='Кнопка "Login" в Book Store Application',
        )


        self.book_store_table_rows = ComponentList(
            page,
            selector=".rt-tbody .rt-tr-group",
            allure_name="Строки таблицы с книгами в Book Store Application",
        )


    def go_to_elements(self):
        # review: нейминг методов должен отвечать на вопрос, что делает? - Переходит в раздел... и далее по коду
        """Переход в раздел Elements."""
        self.button_elements_card.click()
        # review: "**/elements*" лучше перенести в отдельную константу, например src-> helper->urls
        #self.page.wait_for_url(ConstUrl.elements_uri, timeout=15000)
        self.page.wait_for_url("**/elements*", timeout=15000)

    def go_to_book_store(self):
        """Переход в раздел Book Store Application."""
        self.button_book_store_card.click()
        # review: "**/books*" лучше перенести в отдельную константу, например src-> helper->urls
        #self.page.wait_for_url(ConstUrl.books_uri, timeout=15000)
        self.page.wait_for_url("**/books*", timeout=15000)



    def open_elements(self):
        # review: а для чего эта обёртка, почему сразу не вызывать метод go_to_elements, ведь по факту это и происходит
        # review: этот метод не используется в тестах, он не должен быть в репозитории
        """Обёртка для совместимости с тестом."""
        self.go_to_elements()

    def open_book_store(self):
        """Обёртка для совместимости с тестом."""
        self.go_to_book_store()
