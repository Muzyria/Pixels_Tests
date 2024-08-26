from pages_chrome import PageChrome


class AssetsSyncWise360(PageChrome):

    SPINNER = ("xpath", "//div[@class='loader']")

    @staticmethod
    def _get_name_car(name_car: str) -> tuple[str, str]:
        return "xpath", f'//td[text()="Car{name_car}"]'

    def __init__(self) -> None:
        super().__init__()

    def check_spinner_is_invisible(self):
        self.visibility_of_element_located(self.SPINNER)
        self.invisibility_of_element_located(self.SPINNER)
        print("spinner is invisible _____after CART NAME")

    def click_name_car_in_list(self, name_car: str) -> None:
        self.element_to_be_clickable(self._get_name_car(name_car)).click()
        self.check_spinner_is_invisible()



