from selenium.webdriver.common.by import By


def test_check_button_add_to_basket_is_exist(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Button is not displayed"

    # Альтернативный вариант
    # add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    # assert len(add_to_basket_button) == 1, "Button is not displayed"
