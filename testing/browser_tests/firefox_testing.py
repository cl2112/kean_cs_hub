from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import time as t

from browser_variables import Browser_Variables as b_var

from Navbar_Tests import Navbar_Tests

navbar_links = [
    ('Home', 'https://www.keancshub.com/home'),
    ('Events', 'https://www.keancshub.com/events'),
    ('Resources', 'https://www.keancshub.com/resources'),
    ('PD for teachers', 'https://www.keancshub.com/pd-for-teachers'),
    ('PRAXIS Submission', 'https://www.keancshub.com/praxis-submission'),
    ('Team', 'https://www.keancshub.com/team'),
    ('News', 'https://www.keancshub.com/news'),
    ('Partners', 'https://www.keancshub.com/partners'),
]

with Firefox() as browser:

    action = ActionChains(browser)
    nbar_tests = Navbar_Tests(browser)

    browser.set_window_size(*b_var.win_size_desktop)

    browser.get(b_var.home_url_prod)

    for link in navbar_links:
        nbar_tests.test_link(link[0], link[1])
          
