from selenium.webdriver import Chrome
from Base.InitiateDriver import Browser

def test_dereferencement_google():
    driver = Browser.startBrowser()
    driver.get("http://www.google.com")
    driver.maximize_window()


if __name__ == "__main__":
    test_dereferencement_google()