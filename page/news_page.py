from common.base import BasePage

'''
企业新闻
'''

login_url = "http://192.168.9.81/enterprise-admin/"
user_loc = ("name", "userName")
pwd_loc = ("name", "passWord")
login_button = ("id", "login")


class NewsPage(BasePage):
    enterprise_mxp = ("link text", "企业名信片")
    news_core = ("link text", "新闻中心")
    news_frame = ("iframeBody")
    news_title = ("id", "newsTitle")
    status_select = ("id", "status")
    list_news = ("xpath", ".//*[@id='roleList']/tbody/tr[1]")
    search_button = ("id", "inquireNews")
    add_button = ("id", "addNews")
    update_button = ("id", "upDteNews")
    delete_button = ("id", "newsDelete")
    see_button = ("id", "newsExamine")
    preview_button = ("id", "newsPreview")
    news_title_loc = ("id", "addNewsTitle")
    content_loc = ("id", "xhe0_iframe")
    file_loc = ("id", "file")
    save_button = ("id", "addNDetermine")
    reset_button = ("id", "addReset")
    return_button = ("id", "addReturn")
    alert_text = ("xpath", ".//*[@id='dvMsgCT']")
    alert_button = ("xpath", ".//*[@id='dvMsgBtns']/input")
    alert_button1 = ("xpath", ".//*[@id='dvMsgBtns']/input[1]")
    alert_button2 = ("xpath", ".//*[@id='dvMsgBtns']/input[2]")
    image_button = ("class name", "up-img")
    close_image = ("class name", "close-upimg")
    alert_button3 = ("css selector", ".del-com.wsdel-ok")
    alert_button4 = ("class name", "wsdel-no")

    def click_enterprise_mxp(self):
        self.click(self.enterprise_mxp)

    def click_news_core(self):
        self.click(self.news_core)

    def switch_frame(self):
        self.switch_iframe(self.news_frame)

    def input_title(self, text):
        self.send_keys(self.news_title, text)

    def click_status_select(self, text):
        self.select_by_text(self.status_select, text)

    def click_search_button(self):
        self.click(self.search_button)

    def click_add(self):
        self.click(self.add_button)

    def click_update_button(self):
        self.click(self.update_button)

    def click_delete_button(self):
        self.click(self.delete_button)

    def click_see_button(self):
        self.click(self.see_button)

    def click_preview_button(self):
        self.click(self.preview_button)

    def input_news_title(self, text):
        self.send_keys(self.news_title_loc, text)

    def input_time(self, js):
        self.js_execute(js)

    def input_content(self, text):
        self.send_keys1(self.content_loc, text)

    def upload_file(self, text):
        self.send_keys(self.file_loc, text)

    def click_save_button(self):
        self.click(self.save_button)

    def click_reset_button(self):
        self.click(self.reset_button)

    def click_return_button(self):
        self.click(self.return_button)

    def click_list_news(self):
        self.click(self.list_news)

    def get_tip(self):
        t = self.get_text(self.alert_text)
        return t

    def click_alert_button(self):
        self.click(self.alert_button)

    def click_alert_button1(self):
        self.click(self.alert_button1)

    def click_alert_button2(self):
        self.click(self.alert_button2)

    def move_to_image(self):
        self.move_to_element(self.image_button)

    def click_close_image(self):
        self.click(self.close_image)

    def click_alert_button3(self):
        self.click(self.alert_button3)

    def click_alert_button4(self):
        self.click(self.alert_button4)

