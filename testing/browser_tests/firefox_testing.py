from selenium.webdriver import Firefox

from browser_variables import Browser_Variables
b_var = Browser_Variables()

with Firefox() as browser:
    browser.set_window_size(*b_var.win_size_phone)

    browser.get('https://www.keancshub.com')

    