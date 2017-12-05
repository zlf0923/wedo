from common.base import BasePage

'''
员工管理
'''


class StaffListPage(BasePage):
    staff_management = ("link text", "员工管理")
    staff_maintenance = ("link text", "员工维护")
    staff_frame = ("iframeBody")
    phone_loc = ("name", "mobile")  # 手机号
    username_loc = ("name", "userName")  # 真实姓名
    department_select_loc = ("id", "departmentSelect")  # 所属部门
    job_loc = ("name", "job")  # 岗位名称
    staffSearchStatus_select_loc = ("id", "staffSearchSelectStatus")  # 认证状态
    staffSearchRole_select_loc = ("id", "staffSearchSelectRole")  # 角色名称
    start_time_loc = ("id", "staffStartTime")  # 开始时间
    end_time_loc = ("id", "staffEndTime")  # 结束时间
    search_button = ("id", "btnSearchStaff")  # 查询


    def input_phone(self, text):
        self.send_keys(self.phone_loc, text)

    def input_name(self, text):
        self.send_keys(self.username_loc, text)

    def input_job(self, text):
        self.send_keys(self.job_loc, text)

    def click_department_select(self, text):
        self.select_by_text(self.department_select_loc, text)

    def click_Status_select(self, text):
        self.select_by_text(self.staffSearchStatus_select_loc, text)

    def click_Role_select(self, text):
        self.select_by_text(self.staffSearchRole_select_loc, text)

    def click_search_button(self):
        self.click(self.search_button)

    def click_staff_management(self):
        self.find_element(self.staff_management).click()

    def click_staff_maintenance(self):
        self.find_element(self.staff_maintenance).click()

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)



