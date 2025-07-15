import pytest
from hw26.dz_classes import FrameOne, FrameTwo

@pytest.mark.usefixtures("web_driver_dz_front")
class TestDzFront:

    def test_frame_one_verification(self, web_driver_dz_front):
        driver = web_driver_dz_front
        driver.switch_to.frame("frame1")
        frame = FrameOne(driver)

        frame.input_field.send_keys("Frame1_Secret")
        frame.verify_input_button.click()

        alert = driver.switch_to.alert
        assert alert.text == "Верифікація пройшла успішно!"
        alert.accept()

        driver.switch_to.default_content()

    def test_frame_two_verification(self, web_driver_dz_front):
        driver = web_driver_dz_front
        driver.switch_to.frame("frame2")
        frame = FrameTwo(driver)

        frame.input_field.send_keys("Frame2_Secret")
        frame.verify_input_button.click()

        alert = driver.switch_to.alert
        assert alert.text == "Верифікація пройшла успішно!"
        alert.accept()

        driver.switch_to.default_content()
