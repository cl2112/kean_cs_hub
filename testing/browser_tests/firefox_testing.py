from selenium.webdriver import Firefox

with Firefox() as browser:

    browser.get('https://www.keancshub.com')

    # for later, https://www.selenium.dev/documentation/webdriver/browser_manipulation/#browser-navigation
    # driver.current_url
    # driver.set_window_size(1024, 768)
    # driver.maximize_window()

    