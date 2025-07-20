import pytest
from hw27.classes import BaseNovaPost



@pytest.mark.usefixtures("web_driver")
class TestParcelReceivedNP:


    def test_np_received(self,web_driver):
        ttn = "20451194735304"

        frame = BaseNovaPost(web_driver)
        frame.input_field.send_keys(ttn)
        frame.search_button.click()

        frame.through_instructions.click()

        assert frame.check_status.text.strip() == "Отримана"





