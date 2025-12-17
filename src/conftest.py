from pathlib import Path
import sys

import pytest
from playwright.sync_api import sync_playwright, Page



# review: это 'костыль' pytest при запуске должен видеть pages, но так как нет файла gitignore и в репозитории
#нет venv, полагаю, что все зависимости установлены в глобальный пайтон, а не в виртуальное окружение (P.S. venv пушить
#в репозиторий не нужно) возможно в этом проблема

# Путь до папки src
BASE_DIR = Path(__file__).parent
# добавляем src в sys.path, чтобы видеть пакет pages
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# review: Все импорты должны быть сверху (# noqa: E402)
from pages.demoqa_for_python_main import DemoqaForPythonMain  # noqa: E402


@pytest.fixture(scope="session")
def browser() -> Page:
    """Создаём один инстанс браузера Chromium на сессию."""
    # review: для чего файл config_browser.yml в репозитории, если использует page не из коробки (qpn_qa_utils)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="function")
def demoqa_for_python_main(browser: Page) -> DemoqaForPythonMain:
    """Главная страница https://demoqa.com."""
    # review: это лишний комментарий, вероятно от AI
    # на каждый тест создаём новый PageObject, но используем тот же page
    return DemoqaForPythonMain(browser)
