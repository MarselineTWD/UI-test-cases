from pathlib import Path
import sys

import pytest
from playwright.sync_api import sync_playwright, Page

# Путь до папки src
BASE_DIR = Path(__file__).parent

# добавляем src в sys.path, чтобы видеть пакет pages
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from pages.demoqa_for_python_main import DemoqaForPythonMain  # noqa: E402


@pytest.fixture(scope="session")
def browser() -> Page:
    """Создаём один инстанс браузера Chromium на сессию."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="function")
def demoqa_for_python_main(browser: Page) -> DemoqaForPythonMain:
    """Главная страница https://demoqa.com."""
    # на каждый тест создаём новый PageObject, но используем тот же page
    return DemoqaForPythonMain(browser)
