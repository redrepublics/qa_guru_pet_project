import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def base_url(item):
    base_url_test = ["https://www.selenium.dev/", "https://github.com/"]
    return base_url_test[item]


def test_selenium_web(driver):
    url = base_url(0)
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


def test_git_web(driver):
    url = base_url(1)
    driver.get(url)
    assert (
        driver.title
        == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub · GitHub"
    )
    assert driver.current_url == url
