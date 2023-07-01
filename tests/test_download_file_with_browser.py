import time
import os
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


def test_download_with_browser():
    path_main = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    options = webdriver.ChromeOptions()
    prefs = {
    "download.default_directory":  os.path.join(path_main, 'tmp'),
    "download.prompt_for_download": False
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(3)
    assert os.path.exists(os.path.join(os.path.join(path_main, 'tmp'), 'pytest-main.zip')) is True
