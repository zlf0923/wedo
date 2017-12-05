from common.base import BasePage

'''
企业简介
'''


class IntroductionPage(BasePage):
    enterprise_mxp = ("link text", "企业名信片")
    enterprises_introduction = ("link text", "企业简介")
    staff_frame = ("iframeBody")
    content_text = ("id", "message")
    edit_button = ("id", "edit_aboutus")
    content_loc = ("id", "xhe0_iframe")
    image_button = ("css selector", ".xheIcon.xheBtnImg")
    upload_button = ("class name", "xheBtn")
    text_loc = ("id", "xheImgAlt")
    save_button = ("id", "save")
    back_button = ("id", "back")

    def click_enterprise_mxp(self):
        self.click(self.enterprise_mxp)

    def click_brand_introduce(self):
        self.click(self.enterprises_introduction)

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)

    def click_edit_button(self):
        self.click(self.edit_button)

    def input_content(self, text):
        self.send_keys1(self.content_loc, text)

    def click_image(self):
        self.click(self.image_button)

    def input_text(self, text):
        self.send_keys(self.text_loc, text)

    def move_to_image(self):
        self.move_to_element(self.image_button)

    def click_upload_button(self):
        self.click(self.upload_button)

    def js_click_upload(self, js):
        self.js_execute(js)

    def is_click_upload(self):
        s = self.is_clickabke(self.upload_button)
        return s

    def upload_image(self, text):
        self.send_keys1(self.upload_button, text)

    def click_save_button(self):
        self.click(self.save_button)

    def click_back_button(self):
        self.click(self.back_button)
