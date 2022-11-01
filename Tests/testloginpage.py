import time
import pytest
from Locators.CartPageLocator import place_order_btn
from Locators.ProfilePageLocators import *
from Locators.SearchPageLocators import *
from Utilities.LoginUtility import *


@pytest.mark.usefixtures("initiate_driver")
class TestLoginPage:
    def test_login_page_using_correct_phone_and_correct_password(self):
        Find = Util()
        LoginUtility().perform_login_with(username, password)
        assert Find.find(profile_login).is_displayed(), 'Working for correct phone and correct password'

    def test_login_using_wrong_phone_and_correct_pass(self, initiate_driver):
        Find = Util()
        LoginUtility().perform_login_with(invalid_username, password)
        Find.wait_for(incorrect_statement_password)
        incorrect_statement = Find.find(incorrect_statement_password)
        assert incorrect_statement.is_displayed(), 'Working for wrong phone and correct password'

    def test_login_using_wrong_pass_correct_phone(self):
        Find = Util()
        LoginUtility().perform_login_with(username, invalid_password)
        Find.wait_for(incorrect_statement_password)
        incorrect_statement = Find.find(incorrect_statement_password)
        assert incorrect_statement.is_displayed(), 'Working for correct phone and wrong password'

    def test_login_using_wrong_pass_wrong_phone(self):
        Find = Util()
        LoginUtility().perform_login_with(invalid_username, invalid_password)
        Find.wait_for(incorrect_statement_password)
        incorrect_statement = Find.find(incorrect_statement_password)
        assert incorrect_statement.is_displayed(), 'Working for wrong phone and wrong password'
