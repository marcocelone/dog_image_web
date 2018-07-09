from pages.home.dog_api import HomePage
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DogTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.dog_api = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_homepage(self):
        self.dog_api.verify_home_page()

    @pytest.mark.run(order=1)
    def test_verify_side_nav(self):
        self.dog_api.verify_sidenave_menu()

    @pytest.mark.run(order=1)
    def test_verify_side_nav_elements(self):
        self.dog_api.verify_side_menu_elements()

    @pytest.mark.run(order=1)
    def test_documentation_page(self):
        self.dog_api.documentation_page()
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_existing_email_neg(self):
        self.dog_api.subscribed_email()

    @pytest.mark.run(order=1)
    def test_fetch_funcionality(self):
        self.dog_api.fetch_button_functionality()

    #Negative testcase
    @pytest.mark.run(order=1)
    def test_join_email(self):
        self.dog_api.join_new_email()








