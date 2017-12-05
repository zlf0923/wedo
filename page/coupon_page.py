from common.base import BasePage

'''
优惠规则
'''


class CouponPage(BasePage):
    preferential_rules = ("link text", "优惠规则")
    enterprises_preferential_rules = ("link text", "企业优惠规则")
    staff_frame = ("iframeBody")
    list_preferential_name = ("id", "graceName")
    list_shop_name = ("id", "shopName")
    list_type_select = ("id", "type")
    list_status_select = ("id", "status")
    list_preferential = ("xpath", ".//*[contains(text(),'打折优惠')]")
    search_button = ("id", "preferential-search")  # 查询
    add_button = ("id", "preferential-add")  # 添加
    editor_button = ("id", "preferential-editor")  # 修改
    delete_button = ("id", "preferential-delete")  # 删除
    see_button = ("id", "preferential-detile")  # 查看
    shop_name_select = ("id", "ms")
    choice_shop = ("class name", "ms-choice")
    shop_name = ("class name", "ms-select-all")
    preferential_name = ("id", "addgraceName")  # 优惠名称
    money_loc = ("id", "addsingMoney")  # 优惠条件
    full_radio = ("id", "fullDownradio")  # 满减优惠
    reduction_loc = ("id", "addreduction")  # 满减金额
    discounted_radio = ("id", "Discountedradio")  # 打折优惠
    discount_loc = ("id", "adddiscount")  # 折扣
    remark_loc = ("id", "addremark")  # 规则说明
    save_button = ("id", "addokBtn")  # 确定
    back_button = ("id", "addbackBtn")  # 返回
    back_button1 = ("id", "detailbackBtn")  # 查看页面返回
    alert = ("id", "dvMsgBox")
    alert_text = ("xpath", ".//*[@id='dvMsgCT']")
    alert_button = ("xpath", ".//*[@id='dvMsgBtns']/input")
    alert_button1 = ("xpath", ".//*[@id='dvMsgBtns']/input[1]")
    alert_button2 = ("xpath", ".//*[@id='dvMsgBtns']/input[2]")

    def input_list_preferential_name(self, text):
        self.send_keys(self.list_preferential_name, text)

    def input_list_shop_name(self, text):
        self.send_keys(self.list_shop_name, text)

    def select_type(self, text):
        self.select_by_text(self.list_type_select, text)

    def select_status(self, text):
        self.select_by_text(self.list_status_select, text)

    def click_preferential_rules(self):
        self.click(self.preferential_rules)

    def click_enterprises_preferential_rules(self):
        self.click(self.enterprises_preferential_rules)

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)

    def click_search_button(self):
        self.click(self.search_button)

    def click_add_button(self):
        self.click(self.add_button)

    def click_editor_button(self):
        self.click(self.editor_button)

    def click_delete_button(self):
        self.click(self.delete_button)

    def is_click_delete_button(self):
        w = self.is_clickabke(self.delete_button)
        return w

    def is_alert_exists(self):
        r = self.is_exists(self.alert)
        return r

    def click_see_button(self):
        self.click(self.see_button)

    def click_shop(self):
        self.click(self.choice_shop)

    def choice_shop_name(self):
        self.click(self.shop_name)

    def input_preferential_name(self, text):
        self.send_keys(self.preferential_name, text)

    def input_time(self, js):
        self.js_execute(js)

    def input_money(self, text):
        self.send_keys(self.money_loc, text)

    def click_discounted_radio(self):
        self.click(self.discounted_radio)

    def input_discount(self, text):
        self.send_keys(self.discount_loc, text)

    def input_reduction(self, text):
        self.send_keys(self.reduction_loc, text)

    def input_remark(self, text):
        self.send_keys(self.remark_loc, text)

    def click_save_button(self):
        self.click(self.save_button)

    def click_back_button(self):
        self.click(self.back_button)

    def click_detail_back_button(self):
        self.click(self.back_button1)

    def get_tip(self):
        t = self.get_text(self.alert_text)
        return t

    def click_list_preferential(self):
        self.click(self.list_preferential)

    def click_alert_button(self):
        self.click(self.alert_button)

    def click_alert_button1(self):
        self.click(self.alert_button1)

    def click_alert_button2(self):
        self.click(self.alert_button2)
