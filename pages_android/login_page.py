# from pages_android import Page
# from credentials import LOGIN_360, PASSWORD_360
#
#
# class LoginPage(Page):
#
#     def __init__(self) -> None:
#         super().__init__()
#
#         self.login_input_id = ''
#         self.password_input_id = ''
#         self.login_button_id = ''
#
#     def login(self) -> None:
#         # login_input_xpath = self.get_input_field_xpath(self.login_input_id)
#         # login_input_field = self.find_element_by_xpath(login_input_xpath)
#         #------------
#         login_input_field = self.find_element_by_id(self.login_input_id)
#         #----------- com.ajaxsystems:id/authLoginEmail
#         self.send_keys(login_input_field, LOGIN_360)
#
#         # password_input_xpath = self.get_input_field_xpath(self.password_input_id)
#         # password_input_field = self.find_element_by_xpath(password_input_xpath)
#         #------ com.ajaxsystems:id/authLoginPassword
#         password_input_field = self.find_element_by_id(self.password_input_id)
#         #-------
#         self.send_keys(password_input_field, PASSWORD_360)
#
#         login_button = self.find_element_by_id(self.login_button_id)
#         login_button.click()
#
#     def get_input_field_xpath(self, resource_id: str) -> str:
#         resource_id = self._get_resource_id(resource_id)
#         return f'//android.widget.EditText[@resource-id="{resource_id}"]'
