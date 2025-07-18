import pytest
import data
from selenium import webdriver

@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    if request.param == "Chrome":
        data.browser_name = "Chrome"
        driver = webdriver.Chrome()
    else:
        data.browser_name = "Firefox"
        driver = webdriver.Firefox()

    yield driver
    driver.quit()