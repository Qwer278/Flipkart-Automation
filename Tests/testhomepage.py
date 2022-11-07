from Locators.CartPageLocator import place_order_btn
from Locators.ProfilePageLocators import *
from Locators.SearchPageLocators import *
from Utilities.LoginUtility import *


@pytest.mark.usefixtures("initiate_driver")
class TestHomePage:

    def test_logout_account(self):
        Find = Util()
        LoginUtility().perform_login_with(username, password)
        Find.move_to(profile).perform()
        Find.wait_for(logout)
        Find.click_on(logout)
        Find.wait_for(profile_login)
        profile_login_btn = Find.find(profile_login)
        assert profile_login_btn.text == 'Login', 'Working for correct phone and correct password'

    def test_search_box(self):
        Find = Util()
        LoginUtility().perform_login_with(username, password)
        LoginUtility().search_item()
        Find.wait_for(filter_text)
        filter_text_on_search = Find.find(filter_text)
        assert filter_text_on_search.is_displayed(), "Search Box not working"

    def test_open_my_profile(self):
        Find = Util()
        LoginUtility().perform_login_with(username, password)
        Find.move_to(profile).perform()
        Find.move_to(profile).click().perform()
        hello_text_on_profile = Find.find(hello_txt)
        assert hello_text_on_profile.is_displayed(), "Not Opening Profile"

    def test_open_cart(self):
        Find = Util()
        LoginUtility().perform_login_with(username, password)
        Find.wait_for(cart)
        Find.click_on(cart)
        place_order_on_cart_page = Find.find(place_order_btn)
        assert place_order_on_cart_page.is_displayed(), "Cart page not opening"

    def test_select_search_item(self):
        Find = Util()
        LoginUtility().search_item()
        Find.wait_for(search_products)
        w = Find.find_all(search_products)
        w[0].click()
        Find.switch_tab_to(1)
        buy_btn_on_search_page = Find.find(go_to_cart_btn)
        assert buy_btn_on_search_page.is_displayed(), "Not selecting Search Item"

    def test_order_item(self):
        Find = Util()
        LoginUtility().search_item()
        Find.wait_for(pincode)
        Find.find(pincode).send_keys("380009")
        Find.wait_for(go_to_cart_btn)
        Find.click_on(go_to_cart_btn)
