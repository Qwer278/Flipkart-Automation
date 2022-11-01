from . ConfigUtil import *
import time

class LoginUtility:
    def perform_login_with(self,username,password):
        Find = Util()
        Find.find(email).send_keys(username)
        Find.find(pass_inp).send_keys(password)
        Find.click_on(login_btn)

    def search_item(self):
        Find=Util()
        time.sleep(3)
        Find.wait_for(search)
        Find.find(search).send_keys(item_to_be_search)
        Find.click_on(search_btn)
        Find.wait_for(search_products)
        products = Find.find_all(search_products)
        products[0].click()
        Find.switch_tab_to(1)