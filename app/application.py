from selenium import webdriver
from pages.admin_panel_login_page import AdminPanelLoginPage
from pages.customer_list_page import CustomerListPage
from pages.registration_page import RegistrationPage

from pages.product_list_page import ProductListPage
from pages.cart_page import CartPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.registration_page = RegistrationPage(self.driver)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.customer_list_page = CustomerListPage(self.driver)

        self.product_list_page =ProductListPage(self.driver)
        self.cart_page =CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def register_new_customer(self, customer):
        self.registration_page.open()
        self.registration_page.firstname_input.send_keys(customer.firstname)
        self.registration_page.lastname_input.send_keys(customer.lastname)
        self.registration_page.address1_input.send_keys(customer.address)
        self.registration_page.postcode_input.send_keys(customer.postcode)
        self.registration_page.city_input.send_keys(customer.city)
        self.registration_page.select_country(customer.country)
        self.registration_page.select_zone(customer.zone)
        self.registration_page.email_input.send_keys(customer.email)
        self.registration_page.phone_input.send_keys(customer.phone)
        self.registration_page.password_input.send_keys(customer.password)
        self.registration_page.confirmed_password_input.send_keys(customer.password)
        self.registration_page.create_account_button.click()

    def get_customer_ids(self):
        if self.admin_panel_login_page.open().is_on_this_page():
            self.admin_panel_login_page.enter_username("admin").enter_password("admin").submit_login()
        return self.customer_list_page.open().get_customer_ids()

    def add_new_product_to_cart(self,product):
        self.product_list_page.open()
        self.product_list_page.add_in_cart(product)

    def del_product_from_cart(self,product):
        self.cart_page.open()
        self.cart_page.del_from_cart(product)

    def delete_all_from_cart(self):
        self.cart_page.open()
        self.cart_page.del_all_from_cart()

    def get_quantity_of_product_in_cart_on_prod_page(self):
        self.product_list_page.open()
        return self.product_list_page.numbers_of_prod_in_cart_on_prod_page()

    def add_random_distinct_prod(self,quantity):
        self.product_list_page.open()
        self.product_list_page.add_distinct_random_product(quantity)