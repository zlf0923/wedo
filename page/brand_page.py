from common.base import BasePage

'''
品牌介绍
'''


class BrandPage(BasePage):
    enterprise_mxp = ("link text", "企业名信片")
    brand_introduce = ("link text", "品牌介绍")
    staff_frame = ("iframeBody")
    brand_name = ("id", "brandName")
    brand_content = ("id", "brand")
    edit_button = ("id", "edit")
    name_loc = ("id", "brand-name")
    introduce_loc = ("id", "brand-msg")
    file_button = ("id", "file")
    image_button = ("class name", "up-img")
    save_button = ("id", "save")
    clear_button = ("id", "clear")
    back_button = ("id", "back")
    close_image = ("class name", "close-upimg")
    alert_button3 = ("css selector", ".del-com.wsdel-ok")
    alert_button4 = ("class name", "wsdel-no")

    def click_enterprise_mxp(self):
        self.click(self.enterprise_mxp)

    def click_brand_introduce(self):
        self.click(self.brand_introduce)

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)

    def get_brand_name(self):
        t = self.get_text(self.brand_name)
        return t

    def get_brand_content(self):
        t = self.get_text(self.brand_content)
        return t

    def click_edit_button(self):
        self.click(self.edit_button)

    def input_brand_name(self, text):
        self.send_keys(self.name_loc, text)

    def input_brand_introduce(self, text):
        self.send_keys(self.introduce_loc, text)

    def upload_image(self, text):
        self.send_keys(self.file_button, text)

    def file_is_visibility(self):
        self.is_visibility(self.file_button)

    def file_is_click(self):
        d = self.is_clickabke(self.file_button)
        return d

    def file_is_exists(self):
        z = self.is_exists(self.file_button)
        return z

    def file_is_invisibility(self):
        y = self.is_invisibility(self.file_button)
        return y

    def move_to_image(self):
        self.move_to_element(self.image_button)

    def click_save_button(self):
        self.click(self.save_button)

    def click_clear_button(self):
        self.click(self.clear_button)

    def click_back_button(self):
        self.click(self.back_button)

    def click_close_image(self):
        self.click(self.close_image)

    def click_alert_button3(self):
        self.click(self.alert_button3)

    def click_alert_button4(self):
        self.click(self.alert_button4)

