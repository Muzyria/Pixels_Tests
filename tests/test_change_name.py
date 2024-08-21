from pages_android import MainPage
import pytest

users_list = [
    {'first_name': 'Taras', 'last_name': 'Shevchenko', 'age': 47, 'hubs': {'Hub+', 'Hub', 'Hub2'}},
    {'first_name': 'Stepan', 'last_name': 'Bandera', 'age': 50, 'hubs': {'Hub2+', 'Hub+', 'Hub2'}},
    {'first_name': 'Ivan', 'last_name': 'Puluj', 'age': 72, 'hubs': {'Hub2+', 'Hub+', 'Hub', 'Hub2'}},
    {'first_name': 'Bohdan', 'last_name': 'Khmelnytsky', 'age': 61, 'hubs': {'Hub2+', 'Hub'}},
    {'first_name': 'Viacheslav', 'last_name': 'Chornovil', 'age': 61, 'hubs': {'Hub2', 'Hub Hybrid'}},
    {'first_name': 'Andriy', 'last_name': 'Kuzmenko', 'age': 46, 'hubs': {'Hub', 'Hub2'}}
]


def new_names():
    return [str(i["first_name"] + " " + i["last_name"]) for i in users_list if i["age"] > 50 and "Hub2" in i["hubs"]]


# @pytest.mark.parametrize('new_names', new_names())
# def test_change_name(new_names):
#     but = MainPage().press_menu_button()
#
#     MainPage().press_settings_slide_bar_button()
#     AccountInfo().press_account_info_edit_button()
#     AccountInfoEdit().change_name(new_names)
#     AccountInfoEdit().press_back_button()
#     assert AccountInfo().get_title_value() == new_names



