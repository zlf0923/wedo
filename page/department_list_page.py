from common.base import BasePage

'''
部门管理
'''


class DepartmentListPage(BasePage):
    staff_management = ("link text", "员工管理")
    department_list = ("link text", "部门列表")
    staff_frame = ("iframeBody")
    department_name = ("id", "name")
    department_select = ("id", "departmentSelect")
    department_loc = ("xpath", ".//*[@id='departmentList']/tbody/tr[1]")
    number_select = ("class name", "selectPageSize")
    search_button = ("id", "search_btn")
    add_button = ("id", "add_btn")
    change_button = ("id", "change_btn")
    delete_button = ("id", "clear_btn")
    addpage_department_name = ("id", "addpage_departmentName")
    addpage_confirm_button = ("id", "addpage_confirm")
    addpage_alert_text = ("xpath", ".//*[@id='dvMsgCT']")
    addpage_alert_button = ("xpath", ".//*[@id='dvMsgBtns']/input")

    def click_staff_management(self):
        self.find_element(self.staff_management).click()

    def click_department_list(self):
        self.find_element(self.department_list).click()

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)

    def input_department(self, text):
        self.send_keys(self.department_name, text)

    def click_department_select(self, text):
        self.select_by_text(self.department_select, text)

    def click_number(self, text):
        self.select_by_text(self.number_select, text)

    def click_department(self):
        self.find_element(self.department_loc).click()
        # self.click(self.department_loc)

    def click_search(self):
        self.click(self.search_button)

    def click_add(self):
        self.click(self.add_button)

    def input_addpage_department(self, text):
        self.send_keys(self.addpage_department_name, text)

    def click_save(self):
        self.click(self.addpage_confirm_button)

    def get_tip(self):
        t = self.get_text(self.addpage_alert_text)
        return t

    def click_alert_button(self):
        self.click(self.addpage_alert_button)

    def click_change(self):
        self.click(self.change_button)

    def click_delete(self):
        self.click(self.delete_button)

