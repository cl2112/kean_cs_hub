from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.common import exceptions as ex
from time import sleep

class Navbar_Tests():
    def __init__(self, browser):
        self.browser = browser

    def test_link(self, el_link_text, link_url, check_more = False):
        try:
            if check_more:
                more = self.browser.find_element(By.LINK_TEXT, 'More')
                action = action_chains.ActionChains(self.browser)
                (action
                    .move_to_element_with_offset(more,-200, 0)
                    .move_to_element(more)
                    .perform())
            el = self.browser.find_element(By.LINK_TEXT, el_link_text)
            el.click()
            assert self.browser.current_url == link_url
            print(f'{el_link_text} link in navbar went to correct location.')
        except AssertionError as msg:
            print(msg)
        except ex.NoSuchElementException as msg:
            print(msg)
            if not check_more: 
                self.test_link(el_link_text, link_url, check_more=True)
        except Exception as e:
            print(e)

        self.browser.refresh()
        self.browser.back()
