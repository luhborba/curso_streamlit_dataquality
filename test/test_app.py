import subprocess
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    processo = subprocess.Popen(["streamlit", "run", "main.py"])

    driver = webdriver.Chrome()
    driver.get("http://localhost:8501")
    driver.set_page_load_timeout(10)

    yield driver

    driver.quit()
    processo.kill()


def test_open_app(driver):
    driver.get("http://localhost:8501")
    sleep(2)


def test_title_app(driver):
    driver.get("http://localhost:8501")
    sleep(2)
    assert driver.title == "Validador de CSV"
